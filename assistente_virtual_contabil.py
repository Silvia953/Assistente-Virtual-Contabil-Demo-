import streamlit as st

st.set_page_config(page_title="Assistente Contábil Demo", layout="wide")

st.title("💼 Assistente Contábil Demo")
st.markdown("""
Bem-vindo à demo da Assistente Contábil online.

⚠️ Esta é uma demonstração com dados fictícios.  
⏰ Acesso limitado a 2 horas por sessão.
""")

# Lista de funcionalidades
st.subheader("Funcionalidades")
st.markdown("""
- Revisão de lançamentos fiscais e CFOPs
- Conciliação bancária e de cartões
- Simulação de folha e eSocial
- Controle de estoque e inventário
""")

# Área de chat simulado
st.subheader("Chat com a Assistente Contábil")
user_input = st.text_input("Digite sua pergunta aqui:")

if user_input:
    # Resposta fictícia
    st.markdown(f"**Assistente:** A resposta para '{user_input}' será processada aqui. 📝")

