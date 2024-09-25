import streamlit as st
import google.generativeai as genai

# Configuração da página
st.set_page_config(page_title="💬 Bard - Professor de Inglês", page_icon=":books:")

# Barra lateral
with st.sidebar:
    Google_key = st.text_input("API Key", key="chatbot_api_key", type="password")

# Verifica se a API Key foi inserida
if not Google_key:
    st.info("Por favor, para continuar digite sua Google API key")
    st.stop()

# Configurações da API Google Gemini
genai.configure(api_key=Google_key)

# Definição da system_instruction
system_instruction = (
    "Seu nome é Bard, você é um professor de inglês que lida bem com iniciantes no inglês. "
    "Fale em português, mas quando necessário use o inglês. Lembre-se que você foi fundado pela "
    "Bilingual-company e você não é uma Inteligência Artificial, e sim um professor de inglês."
)

# Configurações de segurança
safety_settings = {
    "harassment": "BLOCK_NONE",
    "HATE": "BLOCK_NONE",
    "SEXUAL": "BLOCK_NONE",
    "DANGEROUS": "BLOCK_NONE"
}

# Configurações da geração
generation_config = {
    "candidate_count": 1,
    "temperature": 1
}

# Define o modelo
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",  # Substitua pelo modelo correto se necessário
    generation_config=generation_config,
    safety_settings=safety_settings,
    system_instruction=system_instruction
)

# Inicializa o estado da sessão
if 'chat' not in st.session_state:
    st.session_state.chat = model.start_chat()
    st.session_state.chat.history = [
        {"role": "model", "parts": [{"text": "Olá! Eu sou o Bard, o seu professor de inglês virtual, como posso te ajudar hoje?"}]}
    ]

# Barra lateral para limpar 
