@echo off
echo ========================================
echo   Fernando Leads - Iniciando Servidor
echo ========================================
echo.
echo Iniciando servidor na porta 8000...
echo Acesse: http://localhost:8000
echo.
echo Pressione Ctrl+C para parar o servidor
echo.

python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload

pause

