from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class LeadCreate(BaseModel):
    nome: str
    telefone: str
    email: Optional[str] = None
    observacoes: Optional[str] = None


class LeadResponse(BaseModel):
    id: int
    nome: str
    telefone: str
    email: Optional[str]
    observacoes: Optional[str]
    data_cadastro: datetime
    ativo: bool
    mensagem_3_dias_enviada: bool
    mensagem_7_dias_enviada: bool
    mensagem_10_meses_enviada: bool
    data_envio_3_dias: Optional[datetime]
    data_envio_7_dias: Optional[datetime]
    data_envio_10_meses: Optional[datetime]

    class Config:
        from_attributes = True


class HistoricoMensagemResponse(BaseModel):
    id: int
    lead_id: int
    tipo_mensagem: str
    mensagem: str
    data_envio: datetime
    status: str
    erro: Optional[str]

    class Config:
        from_attributes = True

