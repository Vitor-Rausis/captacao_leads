from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db, init_db, Lead, HistoricoMensagem
from app.models import LeadCreate, LeadResponse, HistoricoMensagemResponse
from app.scheduler import (
    agendar_mensagem_3_dias,
    agendar_mensagem_7_dias,
    agendar_mensagem_10_meses,
    iniciar_scheduler
)
from datetime import datetime

app = FastAPI(title="Fernando Leads - Sistema de Captação de Leads")

# Inicializa o banco de dados
init_db()

# Mostra informações de configuração na inicialização
from app.database import DB_TYPE, IS_SQLITE, IS_POSTGRESQL
from app.whatsapp import USE_TWILIO

print("\n" + "="*70)
print("🚀 FERNANDO LEADS - Sistema Iniciado")
print("="*70)
print(f"📊 Banco de Dados: {DB_TYPE}")
if IS_SQLITE:
    print("   ⚠️  SQLite detectado - adequado para desenvolvimento")
    print("   💡 Para produção, configure PostgreSQL via variável DATABASE_URL")
elif IS_POSTGRESQL:
    print("   ✅ PostgreSQL detectado - pronto para produção")
print(f"📱 WhatsApp: {'✅ Twilio Configurado' if USE_TWILIO else '⚠️  Modo Desenvolvimento (mensagens apenas logadas)'}")
if not USE_TWILIO:
    print("   💡 Para envios reais, configure variáveis: USE_TWILIO, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN")
print("="*70 + "\n")

# Inicia o scheduler (em thread separada para não bloquear)
try:
    iniciar_scheduler()
    print("✅ Scheduler de mensagens automáticas iniciado")
except Exception as e:
    print(f"⚠️  Aviso: Erro ao iniciar scheduler: {e}")
    print("   O servidor continuará rodando, mas mensagens automáticas podem não funcionar.")

# Monta arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root():
    """Retorna a página principal"""
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()


@app.post("/api/leads", response_model=LeadResponse)
def criar_lead(lead: LeadCreate, db: Session = Depends(get_db)):
    """Cria um novo lead e agenda as mensagens automáticas"""
    # Verifica se já existe lead com esse telefone
    lead_existente = db.query(Lead).filter(Lead.telefone == lead.telefone).first()
    if lead_existente:
        raise HTTPException(status_code=400, detail="Já existe um lead com este telefone")
    
    # Cria o lead
    db_lead = Lead(
        nome=lead.nome,
        telefone=lead.telefone,
        email=lead.email,
        observacoes=lead.observacoes,
        data_cadastro=datetime.now()
    )
    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)
    
    # Agenda as mensagens automáticas
    agendar_mensagem_3_dias(db_lead.id, db_lead.data_cadastro)
    agendar_mensagem_7_dias(db_lead.id, db_lead.data_cadastro)
    agendar_mensagem_10_meses(db_lead.id, db_lead.data_cadastro)
    
    return db_lead


@app.get("/api/leads", response_model=List[LeadResponse])
def listar_leads(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Lista todos os leads"""
    leads = db.query(Lead).filter(Lead.ativo == True).offset(skip).limit(limit).all()
    return leads


@app.get("/api/leads/{lead_id}", response_model=LeadResponse)
def obter_lead(lead_id: int, db: Session = Depends(get_db)):
    """Obtém um lead específico"""
    lead = db.query(Lead).filter(Lead.id == lead_id).first()
    if not lead:
        raise HTTPException(status_code=404, detail="Lead não encontrado")
    return lead


@app.delete("/api/leads/{lead_id}")
def desativar_lead(lead_id: int, db: Session = Depends(get_db)):
    """Desativa um lead (não remove, apenas marca como inativo)"""
    lead = db.query(Lead).filter(Lead.id == lead_id).first()
    if not lead:
        raise HTTPException(status_code=404, detail="Lead não encontrado")
    
    lead.ativo = False
    db.commit()
    return {"message": "Lead desativado com sucesso"}


@app.get("/api/leads/{lead_id}/historico", response_model=List[HistoricoMensagemResponse])
def obter_historico_lead(lead_id: int, db: Session = Depends(get_db)):
    """Obtém o histórico de mensagens de um lead"""
    historico = db.query(HistoricoMensagem).filter(
        HistoricoMensagem.lead_id == lead_id
    ).order_by(HistoricoMensagem.data_envio.desc()).all()
    return historico


@app.post("/api/leads/{lead_id}/reenviar/{tipo_mensagem}")
def reenviar_mensagem(lead_id: int, tipo_mensagem: str, db: Session = Depends(get_db)):
    """Reenvia uma mensagem manualmente"""
    tipos_validos = ['3_dias', '7_dias', '10_meses']
    if tipo_mensagem not in tipos_validos:
        raise HTTPException(status_code=400, detail="Tipo de mensagem inválido")
    
    lead = db.query(Lead).filter(Lead.id == lead_id).first()
    if not lead:
        raise HTTPException(status_code=404, detail="Lead não encontrado")
    
    from app.scheduler import enviar_mensagem_agendada
    enviar_mensagem_agendada(lead_id, tipo_mensagem)
    
    return {"message": f"Mensagem {tipo_mensagem} reenviada com sucesso"}


if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

