import streamlit as st
import requests
import json

st.set_page_config(
    page_title="Tradutor EN-FR",
    page_icon="🌐"
)

st.title("🌐 Tradutor Inglês-Francês")
st.write("Traduza textos do inglês para o francês usando IA")

# Input do texto
input_text = st.text_area("Digite o texto em inglês:", height=150)

if st.button("Traduzir"):
    if input_text:
        try:
            # Fazer requisição para a API
            response = requests.post(
                "http://localhost:8000/api/v1/translate",
                json={"text": input_text}
            )
            
            if response.status_code == 200:
                result = response.json()
                st.success("Tradução:")
                st.write(result["translated_text"])
            else:
                st.error(f"Erro: {response.json()['detail']}")
        
        except Exception as e:
            st.error(f"Erro ao se comunicar com a API: {str(e)}")
    else:
        st.warning("Por favor, digite algum texto para traduzir.")

with st.sidebar:
    st.title("Sobre")
    st.write("""
    Este é um tradutor que utiliza:
    - FastAPI
    - LangChain
    - OpenAI
    - Streamlit
    
    Para traduzir textos do inglês para o francês.
    """)
