from pydantic import BaseModel

class ChatInput(BaseModel):
    message: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "message": "olá"
            }
        }

class ChatResponse(BaseModel):
    response: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "response": "Olá! Como posso ajudar você hoje?"
            }
        }
