from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

# Suporta PostgreSQL (para produção) e SQLite (para desenvolvimento)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./leads.db")

# Ajusta URL do PostgreSQL se necessário (alguns serviços usam postgres://)
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Detecta o tipo de banco de dados
IS_POSTGRESQL = "postgresql" in DATABASE_URL.lower()
IS_SQLITE = "sqlite" in DATABASE_URL.lower()

# Configura o engine baseado no tipo de banco
if IS_SQLITE:
    engine = create_engine(
        DATABASE_URL, 
        connect_args={"check_same_thread": False},
        echo=False
    )
    DB_TYPE = "SQLite (Desenvolvimento)"
elif IS_POSTGRESQL:
    engine = create_engine(
        DATABASE_URL,
        pool_pre_ping=True,  # Verifica conexão antes de usar
        echo=False
    )
    DB_TYPE = "PostgreSQL (Produção)"
else:
    # Fallback para SQLite se não reconhecer
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {},
        echo=False
    )
    DB_TYPE = "Desconhecido"
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    telefone = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=True)
    observacoes = Column(Text, nullable=True)
    data_cadastro = Column(DateTime, default=datetime.now)
    ativo = Column(Boolean, default=True)
    
    # Flags para controle de mensagens enviadas
    mensagem_3_dias_enviada = Column(Boolean, default=False)
    mensagem_7_dias_enviada = Column(Boolean, default=False)
    mensagem_10_meses_enviada = Column(Boolean, default=False)
    
    # Datas de envio das mensagens
    data_envio_3_dias = Column(DateTime, nullable=True)
    data_envio_7_dias = Column(DateTime, nullable=True)
    data_envio_10_meses = Column(DateTime, nullable=True)


class HistoricoMensagem(Base):
    __tablename__ = "historico_mensagens"

    id = Column(Integer, primary_key=True, index=True)
    lead_id = Column(Integer, nullable=False)
    tipo_mensagem = Column(String, nullable=False)  # '3_dias', '7_dias', '10_meses'
    mensagem = Column(Text, nullable=False)
    data_envio = Column(DateTime, default=datetime.now)
    status = Column(String, default='pendente')  # 'pendente', 'enviada', 'erro'
    erro = Column(Text, nullable=True)


def init_db():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

