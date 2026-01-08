# 🚀 Como Colocar o Fernando Leads no Ar (Deploy)

## Opção 1: Render.com (MAIS FÁCIL - Recomendado) ⭐

### Passo a Passo:

1. **Criar conta no GitHub** (se não tiver)
   - Acesse: https://github.com
   - Crie uma conta gratuita

2. **Enviar código para o GitHub**
   - No GitHub, crie um novo repositório chamado `fernando-leads`
   - No terminal, execute:
   ```powershell
   cd C:\Users\Desenvolvedor\Desktop\captacao_leads
   git init
   git add .
   git commit -m "Primeiro commit"
   git branch -M main
   git remote add origin https://github.com/SEU_USUARIO/fernando-leads.git
   git push -u origin main
   ```
   (Substitua SEU_USUARIO pelo seu usuário do GitHub)

3. **Fazer deploy no Render**
   - Acesse: https://render.com
   - Clique em "Get Started for Free"
   - Faça login com sua conta GitHub
   - Clique em "New +" → "Web Service"
   - Selecione seu repositório `fernando-leads`
   - Configure:
     - **Name**: `fernando-leads`
     - **Environment**: `Python 3`
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - Clique em "Create Web Service"
   - Aguarde 5-10 minutos (primeira vez demora mais)

4. **Pronto!**
   - Você receberá uma URL como: `https://fernando-leads.onrender.com`
   - Acesse essa URL no navegador
   - Seu sistema estará no ar! 🎉

---

## Opção 2: Railway.app (Ainda mais rápido)

1. Acesse: https://railway.app
2. Login com GitHub
3. Clique em "New Project"
4. Selecione "Deploy from GitHub repo"
5. Escolha o repositório `fernando-leads`
6. Pronto! Railway faz tudo automaticamente
7. Você receberá uma URL automaticamente

---

## ⚙️ Configurar WhatsApp (Opcional)

Se quiser que as mensagens sejam enviadas de verdade via WhatsApp:

1. **Criar conta no Twilio**
   - Acesse: https://www.twilio.com
   - Crie uma conta gratuita (tem créditos para testar)

2. **Configurar no Render/Railway**
   - No painel do serviço, vá em "Environment" ou "Variables"
   - Adicione estas variáveis:
     ```
     USE_TWILIO=true
     TWILIO_ACCOUNT_SID=seu_account_sid_aqui
     TWILIO_AUTH_TOKEN=seu_auth_token_aqui
     TWILIO_WHATSAPP_FROM=whatsapp:+14155238886
     ```
   - Salve e reinicie o serviço

**Sem essas variáveis**, o sistema funciona normalmente, mas as mensagens são apenas logadas (não enviadas de verdade).

---

## 📝 Checklist Rápido

- [ ] Código no GitHub
- [ ] Conta no Render ou Railway
- [ ] Deploy feito
- [ ] URL funcionando
- [ ] Testado adicionar um lead
- [ ] (Opcional) WhatsApp configurado

---

## 🆘 Problemas?

### "Erro ao fazer deploy"
- Verifique se todos os arquivos estão no GitHub
- Veja os logs no painel do Render/Railway

### "Site não carrega"
- Aguarde alguns minutos (primeira vez demora)
- Verifique os logs do serviço

### "Mensagens não são enviadas"
- Verifique se configurou as variáveis do Twilio
- Sem Twilio, mensagens são apenas logadas (modo desenvolvimento)

---

## 💡 Dica

**Render.com** é gratuito e perfeito para começar:
- ✅ Gratuito para sempre
- ✅ HTTPS automático
- ✅ Deploy automático quando você atualiza o código
- ✅ Fácil de usar

**Limitação**: O serviço "dorme" após 15 minutos de inatividade (plano gratuito). A primeira requisição após dormir pode demorar ~30 segundos para "acordar".

---

## 🎯 Próximos Passos

Depois do deploy:
1. Teste adicionar alguns leads
2. Verifique se as mensagens estão sendo agendadas
3. Configure o WhatsApp se quiser envios reais
4. Compartilhe a URL com quem precisa usar!

