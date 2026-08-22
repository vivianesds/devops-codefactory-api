# CodeFactory Solutions - Plataforma Web API

## Descrição do Projeto
API REST desenvolvida para padronizar o fluxo de entregas, melhorar a colaboração e modernizar a arquitetura da CodeFactory Solutions.

## Objetivo
Implementar a cultura DevOps através de processos automatizados, versionamento organizado e infraestrutura containerizada.

## Tecnologias Utilizadas
* Python 3.11 / FastAPI
* Docker & Docker Compose
* GitHub Actions (CI)
* Git / GitHub

## Estrutura de Pastas
```text
├── .github/workflows/ci.yml
├── app/
│   ├── main.py
│   └── test_main.py
├── Dockerfile
├── requirements.txt
└── README.md

## Instruções de Instalação e Execução

### Pré-requisitos
* Python 3.11+ ou Docker instalado no sistema.

### Execução com Python
```bash
# Clone o repositório
git clone https://github.com/vivianesds/devops-codefactory-api.git

# Acesse o diretório
cd devops-codefactory-api

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
python app/main.py
```

### Execução via Docker
```bash
# Construa a imagem
docker build -t codefactory-api .

# Execute o container
docker run -d -p 8000:8000 --name container-codefactory codefactory-api
```

## Licença
Este projeto está sob a licença MIT - consulte o arquivo LICENSE para mais detalhes.
- Alteração feita exclusivamente na branch feature.- Alteração na branch desenvolvimento.