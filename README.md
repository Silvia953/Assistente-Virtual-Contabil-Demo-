import os
import openai
import streamlit as st

# Configure the OpenAI key (must be set in Streamlit Secrets)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Page configuration
st.set_page_config(page_title="Assistente Virtual Contábil Demo", layout="wide")

# Title and welcome message
st.title("💼 Assistente Virtual Contábil Demo")
st.markdown("""
Welcome to the Virtual Accounting Assistant demo.

⚠️ This is a demonstration with fictitious data.  
⏰ Access limited to 2 hours per session.
""")

# Features
st.subheader("Features")
st.markdown("""
- Review of accounting entries and CFOPs  
- Bank and credit card reconciliation  
- Payroll and eSocial simulation  
- Inventory and stock management  
""")

# Chat with the assistant
st.subheader("Chat with the Accounting Assistant")
user_input = st.text_input("Type your question here:")

if user_input:
    try:
        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        st.markdown(f"**Assistant:** {response['choices'][0]['message']['content']}")
    except Exception as e:
        st.error(f"Error generating response: {e}")

.
