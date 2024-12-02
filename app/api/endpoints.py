from fastapi import APIRouter
from app.models.schemas import ChatInput, ChatResponse
from app.core.fake_llm import ChatFakeLLM

router = APIRouter()
chat_llm = ChatFakeLLM()

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(chat_input: ChatInput):
    """
    Endpoint para processar mensagens do chat e retornar respostas
    """
    response = chat_llm.get_response(chat_input.message)
    return ChatResponse(response=response)
