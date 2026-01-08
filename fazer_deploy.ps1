# Script para fazer deploy do Fernando Leads
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Fernando Leads - Deploy Automático" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verifica se Git está instalado
try {
    $gitVersion = git --version
    Write-Host "✅ Git encontrado: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Git não encontrado! Instale o Git primeiro." -ForegroundColor Red
    Write-Host "Download: https://git-scm.com/download/win" -ForegroundColor Yellow
    exit 1
}

Write-Host ""
Write-Host "📝 PASSO 1: Criar repositório no GitHub" -ForegroundColor Yellow
Write-Host ""
Write-Host "1. Acesse: https://github.com/new" -ForegroundColor Cyan
Write-Host "2. Nome do repositório: fernando-leads" -ForegroundColor White
Write-Host "3. Marque como Público (ou Privado)" -ForegroundColor White
Write-Host "4. NÃO marque 'Add README' (já temos)" -ForegroundColor White
Write-Host "5. Clique em 'Create repository'" -ForegroundColor White
Write-Host ""

$prosseguir = Read-Host "Já criou o repositório no GitHub? (s/n)"

if ($prosseguir -ne "s" -and $prosseguir -ne "S") {
    Write-Host ""
    Write-Host "⏸️  Crie o repositório primeiro e depois execute este script novamente." -ForegroundColor Yellow
    Write-Host ""
    pause
    exit
}

Write-Host ""
Write-Host "📝 PASSO 2: Informar URL do repositório" -ForegroundColor Yellow
Write-Host ""
Write-Host "Exemplo: https://github.com/seu-usuario/fernando-leads.git" -ForegroundColor Gray
Write-Host ""

$repoUrl = Read-Host "Cole a URL do seu repositório GitHub"

if ([string]::IsNullOrWhiteSpace($repoUrl)) {
    Write-Host "❌ URL inválida!" -ForegroundColor Red
    pause
    exit
}

Write-Host ""
Write-Host "🔗 Conectando ao repositório..." -ForegroundColor Cyan

# Remove remote se já existir
git remote remove origin -ErrorAction SilentlyContinue

# Adiciona o remote
git remote add origin $repoUrl

Write-Host "✅ Repositório conectado!" -ForegroundColor Green
Write-Host ""
Write-Host "📤 Enviando código para o GitHub..." -ForegroundColor Cyan

try {
    git push -u origin main
    Write-Host ""
    Write-Host "✅ Código enviado com sucesso!" -ForegroundColor Green
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "  PRÓXIMO PASSO: Deploy no Render" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "1. Acesse: https://render.com" -ForegroundColor Cyan
    Write-Host "2. Login com GitHub" -ForegroundColor White
    Write-Host "3. 'New +' → 'Web Service'" -ForegroundColor White
    Write-Host "4. Selecione: fernando-leads" -ForegroundColor White
    Write-Host "5. Configure:" -ForegroundColor White
    Write-Host "   Build: pip install -r requirements.txt" -ForegroundColor Gray
    Write-Host "   Start: uvicorn app.main:app --host 0.0.0.0 --port `$PORT" -ForegroundColor Gray
    Write-Host "6. 'Create Web Service'" -ForegroundColor White
    Write-Host "7. Aguarde 5-10 minutos" -ForegroundColor White
    Write-Host "8. PRONTO! 🎉" -ForegroundColor Green
    Write-Host ""
} catch {
    Write-Host ""
    Write-Host "❌ Erro ao enviar código!" -ForegroundColor Red
    Write-Host "Verifique:" -ForegroundColor Yellow
    Write-Host "  - Se o repositório existe no GitHub" -ForegroundColor White
    Write-Host "  - Se você tem permissão para fazer push" -ForegroundColor White
    Write-Host "  - Se precisa fazer login no Git" -ForegroundColor White
    Write-Host ""
    Write-Host "Para fazer login no Git:" -ForegroundColor Cyan
    Write-Host "  git config --global user.name 'Seu Nome'" -ForegroundColor Gray
    Write-Host "  git config --global user.email 'seu@email.com'" -ForegroundColor Gray
    Write-Host ""
}

pause

