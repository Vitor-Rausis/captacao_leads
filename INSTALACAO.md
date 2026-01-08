# Guia de Instalação - Sistema de Captação de Leads

## Pré-requisitos

### 1. Instalar Python

O Python não está instalado no seu sistema. Siga um dos métodos abaixo:

#### Opção A: Instalar via Microsoft Store (Mais fácil)
1. Abra a Microsoft Store
2. Procure por "Python 3.11" ou "Python 3.12"
3. Clique em "Instalar"
4. Após a instalação, reinicie o terminal

#### Opção B: Instalar via site oficial (Recomendado)
1. Acesse: https://www.python.org/downloads/
2. Baixe a versão mais recente do Python (3.11 ou superior)
3. **IMPORTANTE**: Durante a instalação, marque a opção "Add Python to PATH"
4. Complete a instalação
5. Reinicie o terminal

### 2. Verificar Instalação

Após instalar o Python, verifique se está funcionando:

```powershell
python --version
```

Deve mostrar algo como: `Python 3.11.x` ou `Python 3.12.x`

## Instalação do Projeto

### 1. Instalar Dependências

```powershell
python -m pip install -r requirements.txt
```

### 2. Configurar Variáveis de Ambiente (Opcional)

Se quiser usar WhatsApp real via Twilio:
1. Copie o arquivo `env.example` para `.env`
2. Edite o arquivo `.env` com suas credenciais do Twilio

Se não configurar, o sistema funcionará em modo desenvolvimento (apenas loga as mensagens).

### 3. Executar o Projeto

```powershell
python run.py
```

Ou:

```powershell
python -m uvicorn app.main:app --reload
```

### 4. Acessar a Interface

Abra seu navegador em: **http://localhost:8000**

## Solução de Problemas

### Erro: "Python não foi encontrado"
- Certifique-se de que o Python está instalado
- Verifique se marcou "Add Python to PATH" durante a instalação
- Reinicie o terminal após instalar

### Erro: "pip não é reconhecido"
- Use: `python -m pip` ao invés de apenas `pip`
- Ou instale o pip: `python -m ensurepip --upgrade`

### Erro ao instalar dependências
- Atualize o pip: `python -m pip install --upgrade pip`
- Tente novamente: `python -m pip install -r requirements.txt`

## Próximos Passos

Após instalar e executar:
1. Acesse http://localhost:8000
2. Adicione seus primeiros leads
3. O sistema agendará automaticamente as mensagens
4. As mensagens serão enviadas nos prazos configurados (3 dias, 7 dias, 10 meses)

