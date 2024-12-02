from langchain.llms.fake import FakeListLLM
from typing import List

class ChatFakeLLM:
    def __init__(self):
        # Respostas pré-definidas para simular o comportamento do LLM
        self.responses = {
            "olá": "Olá! Como posso ajudar você hoje?",
            "como vai": "Estou funcionando perfeitamente, obrigado por perguntar!",
            "qual é seu nome": "Meu nome é ChatFake, sou um LLM simulado para testes.",
            "tchau": "Até logo! Foi um prazer conversar com você!"
        }
        
        # Inicializa o FakeListLLM com as respostas
        self.fake_llm = FakeListLLM(responses=list(self.responses.values()))

    def get_response(self, input_text: str) -> str:
        # Converte input para minúsculo para fazer a comparação
        input_lower = input_text.lower()
        
        # Procura por uma resposta correspondente
        for key, response in self.responses.items():
            if key in input_lower:
                return response
                
        # Resposta padrão caso nenhuma correspondência seja encontrada
        return "Desculpe, não entendi sua pergunta. Pode reformular?"
