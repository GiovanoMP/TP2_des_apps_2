from fastapi import APIRouter, HTTPException
from ..core.translator import Translator
from ..models.schemas import TranslationRequest, TranslationResponse  # Caminho corrigido
import traceback

router = APIRouter()
translator = Translator()

@router.post("/translate", response_model=TranslationResponse)
async def translate_text(request: TranslationRequest):
    try:
        translated_text = await translator.translate(request.text)
        return TranslationResponse(translated_text=translated_text)
    except Exception as e:
        print(f"Erro detalhado: {traceback.format_exc()}")
        raise HTTPException(
            status_code=500,
            detail=f"Erro na tradução: {str(e)}"
        )
