# 🚀 Guia de Deploy - Fernando Leads

Este guia mostra como hospedar o projeto Fernando Leads em servidores gratuitos.

## Opção 1: Render.com (Recomendado - Mais Fácil)

### Passo 1: Preparar o Repositório
1. Crie uma conta no GitHub (se ainda não tiver)
2. Crie um novo repositório
3. Faça upload dos arquivos do projeto

### Passo 2: Deploy no Render
1. Acesse: https://render.com
2. Faça login com sua conta GitHub
3. Clique em "New +" → "Web Service"
4. Conecte seu repositório do GitHub
5. Configure:
   - **Name**: fernando-leads
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
6. Clique em "Create Web Service"
7. Aguarde o deploy (pode levar 5-10 minutos)

### Passo 3: Configurar Variáveis de Ambiente (Opcional)
Se quiser usar WhatsApp real via Twilio:
1. Vá em "Environment" no painel do Render
2. Adicione as variáveis:
   - `USE_TWILIO=true`
   - `TWILIO_ACCOUNT_SID=seu_account_sid`
   - `TWILIO_AUTH_TOKEN=seu_auth_token`
   - `TWILIO_WHATSAPP_FROM=whatsapp:+14155238886`

### Passo 4: Acessar
Após o deploy, você receberá uma URL como: `https://fernando-leads.onrender.com`

---

## Opção 2: Railway.app

### Passo 1: Criar Conta
1. Acesse: https://railway.app
2. Faça login com GitHub

### Passo 2: Deploy
1. Clique em "New Project"
2. Selecione "Deploy from GitHub repo"
3. Escolha seu repositório
4. Railway detectará automaticamente que é Python
5. O deploy começará automaticamente

### Passo 3: Configurar
1. Vá em "Variables" para adicionar variáveis de ambiente
2. Railway fornecerá uma URL automaticamente

---

## Opção 3: Fly.io

### Passo 1: Instalar Fly CLI
```bash
# Windows (PowerShell)
iwr https://fly.io/install.ps1 -useb | iex
```

### Passo 2: Login
```bash
fly auth login
```

### Passo 3: Deploy
```bash
fly launch
```

Siga as instruções na tela.

---

## Opção 4: PythonAnywhere

### Passo 1: Criar Conta
1. Acesse: https://www.pythonanywhere.com
2. Crie uma conta gratuita

### Passo 2: Upload dos Arquivos
1. Vá em "Files"
2. Faça upload de todos os arquivos do projeto

### Passo 3: Configurar Web App
1. Vá em "Web"
2. Clique em "Add a new web app"
3. Escolha Python 3.10 ou superior
4. Configure o caminho do arquivo WSGI
5. Configure o arquivo WSGI para apontar para `app.main:app`

---

## ⚠️ Importante para Deploy

### Banco de Dados
O projeto usa SQLite por padrão. Para produção, considere:
- **Render**: SQLite funciona, mas dados podem ser perdidos em reinicializações
- **Railway**: Use PostgreSQL (Railway oferece banco gratuito)
- **Fly.io**: Use volumes persistentes

### Para usar PostgreSQL (Recomendado para produção):

1. Adicione ao `requirements.txt`:
```
psycopg2-binary==2.9.9
```

2. Modifique `app/database.py`:
```python
import os
from sqlalchemy import create_engine

# Usa PostgreSQL se disponível, senão SQLite
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./leads.db")

# Se for PostgreSQL, remove o "sqlite:///" e ajusta a URL
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})
```

### Variáveis de Ambiente
Configure no painel do serviço:
- `USE_TWILIO=false` (ou true se tiver credenciais)
- `TWILIO_ACCOUNT_SID=...` (se usar Twilio)
- `TWILIO_AUTH_TOKEN=...` (se usar Twilio)
- `TWILIO_WHATSAPP_FROM=...` (se usar Twilio)

---

## 🎯 Recomendação

**Para começar rápido**: Use **Render.com**
- Gratuito
- Fácil de configurar
- Deploy automático do GitHub
- URL HTTPS automática

**Para produção**: Use **Railway.app** ou **Fly.io**
- Melhor performance
- Mais opções de configuração
- Suporte a bancos de dados

---

## 📝 Checklist de Deploy

- [ ] Código no GitHub
- [ ] Conta criada no serviço de hospedagem
- [ ] Repositório conectado
- [ ] Variáveis de ambiente configuradas (se necessário)
- [ ] Deploy concluído
- [ ] Testado a URL fornecida
- [ ] WhatsApp configurado (se necessário)

---

## 🆘 Problemas Comuns

### Erro: "Module not found"
- Verifique se todas as dependências estão no `requirements.txt`
- Execute `pip freeze > requirements.txt` localmente

### Erro: "Port already in use"
- O serviço deve usar a variável `$PORT` fornecida pelo host
- Já está configurado no código

### Banco de dados não persiste
- Em Render, dados SQLite podem ser perdidos
- Considere usar PostgreSQL para produção

### Mensagens WhatsApp não funcionam
- Verifique as variáveis de ambiente
- Em modo desenvolvimento, mensagens são apenas logadas

---

## 📞 Suporte

Se tiver problemas, verifique:
1. Logs do serviço no painel de controle
2. Se todas as dependências estão instaladas
3. Se as variáveis de ambiente estão corretas

