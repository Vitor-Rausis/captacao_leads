# 🚀 Deploy Rápido - Siga estes passos

## ✅ Passo 1: Código já está pronto! (FEITO)

O código já foi commitado localmente.

## 📝 Passo 2: Criar repositório no GitHub

1. Acesse: https://github.com/new
2. Nome do repositório: `fernando-leads`
3. Marque como **Público** (ou Privado, como preferir)
4. **NÃO** marque "Add a README file" (já temos)
5. Clique em **"Create repository"**

## 🔗 Passo 3: Conectar e enviar código

Depois de criar o repositório, o GitHub mostrará comandos. Execute estes aqui:

```powershell
git remote add origin https://github.com/SEU_USUARIO/fernando-leads.git
git push -u origin main
```

(Substitua SEU_USUARIO pelo seu usuário do GitHub)

## 🌐 Passo 4: Deploy no Render.com

1. Acesse: https://render.com
2. Clique em **"Get Started for Free"**
3. Faça login com sua conta **GitHub**
4. Clique em **"New +"** → **"Web Service"**
5. Selecione o repositório **fernando-leads**
6. Configure:
   - **Name**: `fernando-leads`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
7. Clique em **"Create Web Service"**
8. Aguarde 5-10 minutos
9. **PRONTO!** Você terá uma URL como: `https://fernando-leads.onrender.com`

---

## ⚡ Alternativa Rápida: Railway

1. Acesse: https://railway.app
2. Login com GitHub
3. "New Project" → "Deploy from GitHub repo"
4. Selecione `fernando-leads`
5. Pronto! Railway faz tudo sozinho

---

## 🎯 Próximo Passo

**Crie o repositório no GitHub agora** e me avise quando estiver pronto para eu ajudar a conectar!

Ou se preferir, posso tentar criar via API se você tiver um token do GitHub.

