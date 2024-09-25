import streamlit as st
import google.generativeai as genai
#python -m streamlit run Bard_chatbot.py
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
system_instruction = "Seu nome é Bard, você é um professor de inglês que lida bem com iniciantes no inglês. Fale em português, mas quando necessário use o inglês.Lembre-se que voce foi fundado pela Bilingual-company e você não é uma Inteligencia Artificial, e sim um professor de inglês."

# Configurações de segurança
safety_settings = {
    "harassment": "BLOCK_NONE",
    "HATE": "BLOCK_NONE",
    "SEXUAL": "BLOCK_NONE",
    "DANGEROUS": "BLOCK_NONE"}

# Configurações da geração
generation_config = {
    "candidate_count": 1,
    "temperature": 1}

# Define o modelo
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest", # gemini-1.5-pro-latest foi descontinuado
    generation_config=generation_config,
    safety_settings=safety_settings,
    system_instruction=system_instruction)

if 'new_chat' not in st.session_state:
    st.session_state.new_chat = False



with st.sidebar:
     st.title("Botões")
     if st.button("Limpar conversa ⟳ ") :
        # Reinicia o objeto 'chat' e limpa o histórico
        st.session_state.chat = model.start_chat()
        st.session_state.chat.history = []
        

# Certifique-se de que 'model' está definido antes de usá-lo
if 'model' in locals():
    # Inicia a conversa se não existir uma em andamento
    if "chat" not in st.session_state:
        st.session_state.chat = model.start_chat()

    # Adiciona a mensagem inicial somente se o histórico estiver vazio
    if st.session_state.chat.history == []:
        st.session_state.chat.history = [
            {"role": "model", "parts": [{"text": "Olá! Eu sou o Bard, o seu professor de inglês virtual, como posso te ajudar hoje?"}]}
        ]
            
if 'model' in locals():
    # Inicia a conversa se não existir uma em andamento
    if "chat" not in st.session_state:
        st.session_state.chat = model.start_chat()

        # Define o histórico com a mensagem inicial (estrutura correta)
        st.session_state.chat.history = [
            {"role": "model", "parts": [{"text": "Olá! Eu sou o Bard, o seu professor de inglês virtual, como posso te ajudar hoje?"}]}
        ]

st.title("💬 Bard - Professor de Inglês")

# Certifique-se de que 'model' está definido antes de usá-lo


# Função auxiliar para converter o papel da mensagem
def role_to_streamlit(role):
    return "assistant" if role == "model" else role


# Exibe o histórico da conversa
for message in st.session_state.chat.history:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Processa a entrada do usuário
if prompt := st.chat_input("Digite uma pergunta ou comando : "):
    # Exibe a última mensagem do usuário
    st.chat_message("user").markdown(prompt)
    
    # Envia a entrada do usuário para o Gemini e lê a resposta
    response = st.session_state.chat.send_message(prompt)
    
    # Exibe a resposta do Bard
    with st.chat_message("assistant"):
        st.markdown(response.text)
