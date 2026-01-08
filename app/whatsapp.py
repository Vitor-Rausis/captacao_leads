import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

# Configurações do Twilio (ou outra API de WhatsApp)
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", "")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", "")
TWILIO_WHATSAPP_FROM = os.getenv("TWILIO_WHATSAPP_FROM", "whatsapp:+14155238886")

# Se não usar Twilio, você pode usar outras APIs como Evolution API, etc.
USE_TWILIO = os.getenv("USE_TWILIO", "false").lower() == "true"


def formatar_telefone(telefone: str) -> str:
    """Formata o telefone para o formato internacional do WhatsApp"""
    # Remove caracteres não numéricos
    telefone = ''.join(filter(str.isdigit, telefone))
    
    # Se não começar com +, adiciona código do Brasil (55)
    if not telefone.startswith('+'):
        if telefone.startswith('0'):
            telefone = telefone[1:]
        if not telefone.startswith('55'):
            telefone = '55' + telefone
    
    return f"whatsapp:+{telefone}"


def enviar_mensagem_whatsapp(telefone: str, mensagem: str) -> dict:
    """
    Envia mensagem via WhatsApp usando Twilio ou outra API
    
    Retorna dict com status e mensagem de erro (se houver)
    """
    telefone_formatado = formatar_telefone(telefone)
    
    if USE_TWILIO and TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN:
        try:
            client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
            message = client.messages.create(
                body=mensagem,
                from_=TWILIO_WHATSAPP_FROM,
                to=telefone_formatado
            )
            return {
                "status": "enviada",
                "message_sid": message.sid,
                "erro": None
            }
        except Exception as e:
            return {
                "status": "erro",
                "message_sid": None,
                "erro": str(e)
            }
    else:
        # Modo de desenvolvimento - apenas loga a mensagem
        print(f"\n[MODO DESENVOLVIMENTO - WhatsApp não configurado]")
        print(f"📱 Para: {telefone_formatado}")
        print(f"💬 Mensagem: {mensagem}")
        print(f"{'='*60}\n")
        return {
            "status": "enviada",
            "message_sid": "dev_mode",
            "erro": None
        }


def obter_mensagem_3_dias() -> str:
    """Retorna a mensagem para 3 dias após o cadastro"""
    return "Olá, você tem alguma dúvida sobre os brinquedos, ou tem interesse em fazer a reserva?"


def obter_mensagem_7_dias() -> str:
    """Retorna a mensagem para 7 dias após o cadastro"""
    return "Olá, como vai?\n\nVocê já fez a locação dos brinquedos, ou tem interesse em fazer a locação?"


def obter_mensagem_10_meses() -> str:
    """Retorna a mensagem para 10 meses após o cadastro"""
    return "Olá, sou o Fernando da Diversão Brinquedos, como vai?\n\nA um tempo atrás vc fez a cotação de brinquedos com nosso empresa, quero saber se tem interesse em receber o catálogo atualizado para uma nova locação?"

