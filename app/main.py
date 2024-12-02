from fastapi import FastAPI
from app.api.endpoints import router

app = FastAPI(
    title="Chat Fake LLM API",
    description="API para demonstração de um chatbot usando Fake LLM",
    version="1.0.0"
)

# Incluindo as rotas do chat
app.include_router(router, prefix="/api/v1", tags=["chat"])

# Rota raiz
@app.get("/")
async def root():
    return {
        "message": "Bem-vindo à API do Chat Fake LLM",
        "docs": "/docs",
        "endpoints": {
            "chat": "/api/v1/chat"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
