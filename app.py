import streamlit as st
import google.generativeai as genai

API_KEY = ""
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("models/gemini-2.5-flash")  # modelo gratuito

def gerar_texto(prompt):
    try:
        resposta = model.generate_content("Em português brasileiro gere um texto simples sobre: "+prompt+". Só o texto, e faça uma piadinha de tiozão junto com o texto.")
        return resposta.text
    except Exception as e:
        return f"Erro ao gerar texto: {e}"

st.title("Chefia Text Generator 3000")

prompt = st.text_input("Tema:", placeholder="Ex: Explique a importância da reciclagem")

if st.button("Gerar Texto"):
    if prompt.strip() == "":
        st.warning("Digite um prompt!")
    else:
        with st.spinner("Gerando texto..."):
            texto = gerar_texto(prompt)
        st.write(texto)