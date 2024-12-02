from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_chat_endpoint():
    # Teste com mensagem "olá"
    response = client.post(
        "/api/v1/chat",
        json={"message": "olá"}
    )
    assert response.status_code == 200
    assert "response" in response.json()
    
    # Teste com mensagem desconhecida
    response = client.post(
        "/api/v1/chat",
        json={"message": "mensagem aleatória"}
    )
    assert response.status_code == 200
    assert "response" in response.json()
