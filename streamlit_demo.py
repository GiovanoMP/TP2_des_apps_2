import streamlit as st
import requests
import json

st.set_page_config(
    page_title="Chat Fake LLM",
    page_icon="🤖"
)

st.title("💬 Chat Fake LLM")
st.write("Um chatbot simples usando Fake LLM")

# Inicializar histórico de chat no state se não existir
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar histórico de mensagens
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input do usuário
if prompt := st.chat_input("Digite sua mensagem..."):
    # Adicionar mensagem do usuário ao histórico
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Mostrar mensagem do usuário
    with st.chat_message("user"):
        st.markdown(prompt)

    # Fazer requisição para a API
    try:
        response = requests.post(
            "http://localhost:8000/api/v1/chat",
            json={"message": prompt}
        )
        bot_response = response.json()["response"]
        
        # Adicionar resposta do bot ao histórico
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
        
        # Mostrar resposta do bot
        with st.chat_message("assistant"):
            st.markdown(bot_response)
    
    except Exception as e:
        st.error(f"Erro ao se comunicar com a API: {str(e)}")

# Adicionar informações no sidebar
with st.sidebar:
    st.title("Sobre")
    st.write("""
    Este é um chatbot simples que usa um Fake LLM para demonstração.
    
    Você pode tentar as seguintes mensagens:
    - olá
    - como vai
    - qual é seu nome
    - tchau
    """)
