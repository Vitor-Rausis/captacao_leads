# Script para iniciar o servidor Fernando Leads
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Fernando Leads - Iniciando Servidor" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verifica se Python está instalado
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Python encontrado: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "ERRO: Python não encontrado!" -ForegroundColor Red
    Write-Host "Instale o Python primeiro." -ForegroundColor Yellow
    exit 1
}

Write-Host ""
Write-Host "Iniciando servidor na porta 8000..." -ForegroundColor Yellow
Write-Host "Acesse: http://localhost:8000" -ForegroundColor Cyan
Write-Host ""
Write-Host "Pressione Ctrl+C para parar o servidor" -ForegroundColor Gray
Write-Host ""

# Inicia o servidor
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload

