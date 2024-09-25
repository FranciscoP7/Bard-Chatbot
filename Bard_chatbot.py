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
    "Biling
