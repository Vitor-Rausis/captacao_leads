from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.date import DateTrigger
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.database import Lead, HistoricoMensagem
from app.whatsapp import (
    enviar_mensagem_whatsapp,
    obter_mensagem_3_dias,
    obter_mensagem_7_dias,
    obter_mensagem_10_meses
)

scheduler = BackgroundScheduler()


def agendar_mensagem_3_dias(lead_id: int, data_cadastro: datetime):
    """Agenda mensagem para 3 dias após o cadastro"""
    data_envio = data_cadastro + timedelta(days=3)
    
    # Se a data já passou, agenda para agora
    if data_envio < datetime.now():
        data_envio = datetime.now() + timedelta(seconds=10)
    
    scheduler.add_job(
        enviar_mensagem_agendada,
        trigger=DateTrigger(run_date=data_envio),
        args=[lead_id, '3_dias'],
        id=f'msg_3d_{lead_id}',
        replace_existing=True
    )


def agendar_mensagem_7_dias(lead_id: int, data_cadastro: datetime):
    """Agenda mensagem para 7 dias após o cadastro"""
    data_envio = data_cadastro + timedelta(days=7)
    
    # Se a data já passou, agenda para agora
    if data_envio < datetime.now():
        data_envio = datetime.now() + timedelta(seconds=10)
    
    scheduler.add_job(
        enviar_mensagem_agendada,
        trigger=DateTrigger(run_date=data_envio),
        args=[lead_id, '7_dias'],
        id=f'msg_7d_{lead_id}',
        replace_existing=True
    )


def agendar_mensagem_10_meses(lead_id: int, data_cadastro: datetime):
    """Agenda mensagem para 10 meses após o cadastro"""
    data_envio = data_cadastro + timedelta(days=300)  # ~10 meses
    
    scheduler.add_job(
        enviar_mensagem_agendada,
        trigger=DateTrigger(run_date=data_envio),
        args=[lead_id, '10_meses'],
        id=f'msg_10m_{lead_id}',
        replace_existing=True
    )


def enviar_mensagem_agendada(lead_id: int, tipo_mensagem: str):
    """Envia a mensagem agendada e atualiza o banco de dados"""
    db = SessionLocal()
    try:
        lead = db.query(Lead).filter(Lead.id == lead_id).first()
        
        if not lead or not lead.ativo:
            return
        
        # Verifica se já foi enviada
        if tipo_mensagem == '3_dias' and lead.mensagem_3_dias_enviada:
            return
        if tipo_mensagem == '7_dias' and lead.mensagem_7_dias_enviada:
            return
        if tipo_mensagem == '10_meses' and lead.mensagem_10_meses_enviada:
            return
        
        # Obtém a mensagem
        if tipo_mensagem == '3_dias':
            mensagem = obter_mensagem_3_dias()
        elif tipo_mensagem == '7_dias':
            mensagem = obter_mensagem_7_dias()
        elif tipo_mensagem == '10_meses':
            mensagem = obter_mensagem_10_meses()
        else:
            return
        
        # Envia a mensagem
        resultado = enviar_mensagem_whatsapp(lead.telefone, mensagem)
        
        # Registra no histórico
        historico = HistoricoMensagem(
            lead_id=lead_id,
            tipo_mensagem=tipo_mensagem,
            mensagem=mensagem,
            status=resultado['status'],
            erro=resultado.get('erro')
        )
        db.add(historico)
        
        # Atualiza o lead
        if tipo_mensagem == '3_dias':
            lead.mensagem_3_dias_enviada = True
            lead.data_envio_3_dias = datetime.now()
        elif tipo_mensagem == '7_dias':
            lead.mensagem_7_dias_enviada = True
            lead.data_envio_7_dias = datetime.now()
        elif tipo_mensagem == '10_meses':
            lead.mensagem_10_meses_enviada = True
            lead.data_envio_10_meses = datetime.now()
        
        db.commit()
        
    except Exception as e:
        db.rollback()
        print(f"Erro ao enviar mensagem: {e}")
    finally:
        db.close()


def verificar_mensagens_pendentes():
    """Verifica leads que precisam receber mensagens e agenda se necessário"""
    db = SessionLocal()
    try:
        leads = db.query(Lead).filter(Lead.ativo == True).all()
        agora = datetime.now()
        
        for lead in leads:
            # Mensagem de 3 dias
            if not lead.mensagem_3_dias_enviada:
                data_envio_3d = lead.data_cadastro + timedelta(days=3)
                if data_envio_3d <= agora:
                    enviar_mensagem_agendada(lead.id, '3_dias')
                else:
                    agendar_mensagem_3_dias(lead.id, lead.data_cadastro)
            
            # Mensagem de 7 dias
            if not lead.mensagem_7_dias_enviada:
                data_envio_7d = lead.data_cadastro + timedelta(days=7)
                if data_envio_7d <= agora:
                    enviar_mensagem_agendada(lead.id, '7_dias')
                else:
                    agendar_mensagem_7_dias(lead.id, lead.data_cadastro)
            
            # Mensagem de 10 meses
            if not lead.mensagem_10_meses_enviada:
                data_envio_10m = lead.data_cadastro + timedelta(days=300)
                if data_envio_10m <= agora:
                    enviar_mensagem_agendada(lead.id, '10_meses')
                else:
                    agendar_mensagem_10_meses(lead.id, lead.data_cadastro)
                    
    except Exception as e:
        print(f"Erro ao verificar mensagens pendentes: {e}")
    finally:
        db.close()


def iniciar_scheduler():
    """Inicia o scheduler e verifica mensagens pendentes"""
    if not scheduler.running:
        scheduler.start()
        # Verifica mensagens pendentes a cada hora
        scheduler.add_job(
            verificar_mensagens_pendentes,
            trigger='interval',
            hours=1,
            id='verificar_pendentes'
        )
        # Executa uma verificação imediata
        verificar_mensagens_pendentes()

