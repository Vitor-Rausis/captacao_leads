"""
Script para iniciar o servidor do sistema de captação de leads
"""
import uvicorn

if __name__ == "__main__":
    print("=" * 50)
    print("Fernando Leads - Sistema de Captação de Leads")
    print("=" * 50)
    print("\nServidor iniciando em http://localhost:8000")
    print("Pressione Ctrl+C para parar o servidor\n")
    
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )

