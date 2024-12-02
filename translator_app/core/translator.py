from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

class Translator:
    def __init__(self):
        load_dotenv()
        self.llm = ChatOpenAI()  # Vai usar automaticamente a OPENAI_API_KEY do ambiente

    async def translate(self, text: str) -> str:
        try:
            response = self.llm.invoke(
                f"Translate the following text to Portuguese (Brasil): {text}"
            )
            return response.content
        except Exception as e:
            raise Exception(f"Erro na tradução: {str(e)}")
