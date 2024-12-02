# Exercícios LangChain - Chatbot e Tradutor

## ⚠️ Aviso Importante
**Atualmente estamos enfrentando problemas com a chave da OpenAI. O exercício 2 pode não funcionar conforme esperado até resolvermos esta questão.**

## 📝 Descrição dos Exercícios

### Exercício 1: Chatbot com Fake LLM
Desenvolvimento de um protótipo de chatbot utilizando LangChain com Fake LLM para simulações e testes rápidos.

#### Arquitetura
[Cliente] → [FastAPI] → [LangChain] → [Fake LLM] → [Resposta]

#### Funcionalidades
- Endpoint POST para receber mensagens do usuário
- Processamento via Fake LLM
- Respostas simuladas pré-definidas
- Interface FastAPI para interação

### Exercício 2: Tradutor com OpenAI
Sistema de tradução Inglês-Francês utilizando LangChain integrado com a API da OpenAI.

#### Arquitetura
[Cliente] → [FastAPI] → [LangChain] → [OpenAI API] → [Resposta Traduzida]

#### Funcionalidades
- Endpoint POST para receber textos em inglês
- Integração com OpenAI via LangChain
- Tradução para francês
- Resposta em formato JSON

## 🛠️ Tecnologias Utilizadas
- Python 3.8+
- FastAPI
- LangChain
- OpenAI (temporariamente indisponível)
- Uvicorn

## 📦 Instalação

1. Clone o repositório
git clone [url-do-repositorio]

2. Instale as dependências
pip install -r requirements.txt

3. Configure o ambiente
cp .env.example .env
# Edite o arquivo .env com suas configurações

## 🚀 Como Executar

### Exercício 1 - Chatbot
uvicorn chatbot:app --reload

Exemplo de uso:
curl -X POST "http://localhost:8000/chat" -H "Content-Type: application/json" -d '{"message": "Olá!"}'

### Exercício 2 - Tradutor
uvicorn translator:app --reload

Exemplo de uso:
curl -X POST "http://localhost:8000/translate" -H "Content-Type: application/json" -d '{"text": "Hello world"}'

## 📚 Estrutura do Projeto
.
├── chatbot.py          # Implementação do chatbot com Fake LLM
├── translator.py       # Implementação do tradutor
├── requirements.txt    # Dependências do projeto
├── .env.example       # Exemplo de configurações
└── README.md          # Este arquivo

## ⚙️ Configuração

### Variáveis de Ambiente (.env)
OPENAI_API_KEY=sua_chave_aqui  # Temporariamente com problemas

## 🧪 Testes
Para executar os testes:
pytest

## 📝 Requisitos do Sistema
fastapi>=0.68.0
uvicorn>=0.15.0
langchain>=0.0.200
python-dotenv>=0.19.0
openai>=0.27.0

## 🤝 Contribuições
Contribuições são bem-vindas! Por favor:
1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature
3. Faça o Commit de suas mudanças
4. Faça o Push para a Branch
5. Abra um Pull Request

## 📄 Licença
Este projeto está sob a licença MIT.

## 🐛 Problemas Conhecidos
- A integração com a API da OpenAI está temporariamente indisponível
- Investigando problemas com a autenticação da chave da API

## 📞 Suporte
Para reportar problemas ou tirar dúvidas, abra uma issue no repositório.
