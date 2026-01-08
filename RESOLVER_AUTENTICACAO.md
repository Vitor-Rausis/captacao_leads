# 🔐 Resolver Problema de Autenticação GitHub

## Problema
O Git está tentando usar credenciais de `VitorRausis21` mas o repositório é `Vitor-Rausis`.

## ✅ Solução Rápida: Personal Access Token

### Passo 1: Criar Token no GitHub
1. Acesse: https://github.com/settings/tokens
2. Clique em "Generate new token" → "Generate new token (classic)"
3. Dê um nome: `Fernando Leads Deploy`
4. Marque a opção: **`repo`** (todas as permissões de repositório)
5. Clique em "Generate token"
6. **COPIE O TOKEN** (você só verá uma vez!)

### Passo 2: Limpar Credenciais Antigas
Execute no PowerShell:
```powershell
git credential-manager-core erase
```
Ou no Windows:
- Vá em: Painel de Controle → Credenciais do Windows
- Procure por "github.com"
- Remova as credenciais antigas

### Passo 3: Fazer Push
Execute:
```powershell
git push -u origin main
```

Quando pedir:
- **Usuário**: `Vitor-Rausis`
- **Senha**: Cole o **Personal Access Token** (não sua senha do GitHub!)

---

## 🔄 Alternativa: Usar SSH

### Passo 1: Gerar Chave SSH
```powershell
ssh-keygen -t ed25519 -C "seu@email.com"
```
(Pressione Enter para aceitar o local padrão)

### Passo 2: Copiar Chave Pública
```powershell
cat ~/.ssh/id_ed25519.pub
```
Copie toda a saída

### Passo 3: Adicionar no GitHub
1. Acesse: https://github.com/settings/keys
2. Clique em "New SSH key"
3. Cole a chave pública
4. Salve

### Passo 4: Mudar Remote para SSH
```powershell
git remote set-url origin git@github.com:Vitor-Rausis/captacao_leads.git
git push -u origin main
```

---

## ⚡ Solução Mais Rápida (GitHub CLI)

Se tiver GitHub CLI instalado:
```powershell
gh auth login
gh repo set-default Vitor-Rausis/captacao_leads
git push -u origin main
```

