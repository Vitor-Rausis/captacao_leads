# 🚀 Deploy Rápido - Fernando Leads

## Deploy no Render.com (5 minutos)

### 1. Prepare o código no GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/SEU_USUARIO/fernando-leads.git
git push -u origin main
```

### 2. Deploy no Render
1. Acesse: https://render.com
2. Clique em "New +" → "Web Service"
3. Conecte seu repositório GitHub
4. Configure:
   - **Name**: fernando-leads
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. Clique em "Create Web Service"
6. Aguarde 5-10 minutos
7. Pronto! Você terá uma URL como: `https://fernando-leads.onrender.com`

### 3. Testar
Acesse a URL fornecida no navegador e comece a usar!

---

## ⚡ Deploy no Railway (Ainda mais rápido)

1. Acesse: https://railway.app
2. Login com GitHub
3. "New Project" → "Deploy from GitHub repo"
4. Selecione o repositório
5. Pronto! Railway faz tudo automaticamente

---

## 📱 WhatsApp em Produção

Para usar WhatsApp real, você precisa:
1. Conta no Twilio (https://www.twilio.com)
2. Configurar variáveis de ambiente no painel:
   - `USE_TWILIO=true`
   - `TWILIO_ACCOUNT_SID=...`
   - `TWILIO_AUTH_TOKEN=...`
   - `TWILIO_WHATSAPP_FROM=...`

Sem essas variáveis, o sistema funciona em modo desenvolvimento (apenas loga mensagens).

