# Fernando Leads - Sistema de Captação de Leads

Sistema automatizado para captação e acompanhamento de leads com envio automático de mensagens via WhatsApp.

## Funcionalidades

- ✅ Cadastro de leads com informações de contato
- ✅ Envio automático de mensagens via WhatsApp:
  - **3 dias** após o cadastro: "Olá, você tem alguma dúvida sobre os brinquedos, ou tem interesse em fazer a reserva?"
  - **7 dias** após o cadastro: "Olá, como vai? Você já fez a locação dos brinquedos, ou tem interesse em fazer a locação?"
  - **10 meses** após o cadastro: "Olá, sou o Fernando da Diversão Brinquedos, como vai? A um tempo atrás vc fez a cotação de brinquedos com nosso empresa, quero saber se tem interesse em receber o catálogo atualizado para uma nova locação?"
- ✅ Interface web para gerenciar leads
- ✅ Histórico de mensagens enviadas
- ✅ Sistema de agendamento automático

## Instalação

1. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

2. **Configure as variáveis de ambiente:**
   - Copie o arquivo `.env.example` para `.env`
   - Se usar Twilio, configure as credenciais
   - Se não usar Twilio, o sistema funcionará em modo desenvolvimento (apenas loga as mensagens)

3. **Execute o servidor:**
```bash
python -m uvicorn app.main:app --reload
```

4. **Acesse a interface:**
   - Abra o navegador em: `http://localhost:8000`

## Configuração do WhatsApp

### Opção 1: Twilio (Recomendado para produção)

1. Crie uma conta no [Twilio](https://www.twilio.com/)
2. Configure o WhatsApp Sandbox ou use a API oficial
3. Adicione as credenciais no arquivo `.env`:
```
USE_TWILIO=true
TWILIO_ACCOUNT_SID=seu_account_sid
TWILIO_AUTH_TOKEN=seu_auth_token
TWILIO_WHATSAPP_FROM=whatsapp:+14155238886
```

### Opção 2: Modo Desenvolvimento

Se não configurar o Twilio, o sistema funcionará em modo desenvolvimento, apenas logando as mensagens no console. Isso é útil para testes.

### Opção 3: Outras APIs

Você pode modificar o arquivo `app/whatsapp.py` para integrar com outras APIs de WhatsApp como:
- Evolution API
- WhatsApp Business API
- Baileys
- etc.

## Estrutura do Projeto

```
captacao_leads/
├── app/
│   ├── __init__.py
│   ├── main.py              # API FastAPI principal
│   ├── database.py          # Modelos e configuração do banco
│   ├── models.py            # Modelos Pydantic
│   ├── whatsapp.py          # Integração com WhatsApp
│   └── scheduler.py         # Agendamento de mensagens
├── static/
│   └── index.html           # Interface web
├── requirements.txt         # Dependências Python
├── .env.example            # Exemplo de configuração
└── README.md               # Este arquivo
```

## API Endpoints

- `GET /` - Interface web
- `POST /api/leads` - Criar novo lead
- `GET /api/leads` - Listar todos os leads
- `GET /api/leads/{id}` - Obter lead específico
- `DELETE /api/leads/{id}` - Desativar lead
- `GET /api/leads/{id}/historico` - Histórico de mensagens
- `POST /api/leads/{id}/reenviar/{tipo}` - Reenviar mensagem manualmente

## Banco de Dados

O sistema usa SQLite por padrão. O arquivo `leads.db` será criado automaticamente na primeira execução.

## Notas Importantes

- O sistema agenda as mensagens automaticamente quando um lead é cadastrado
- Mensagens são enviadas automaticamente nos horários agendados
- O sistema verifica mensagens pendentes a cada hora
- Leads podem ser desativados (não são removidos, apenas marcados como inativos)

## Suporte

Para dúvidas ou problemas, verifique:
1. Se o scheduler está rodando
2. Se as credenciais do WhatsApp estão corretas
3. Se o formato do telefone está correto (deve incluir código do país)

