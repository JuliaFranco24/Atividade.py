import streamlit as st
lista=st.columns(4)

nome=st.text_input('Digite seu nome')
email=st.text_input('Digite seu email')

st.write(nome)

if st.button('enviar'):
    if email=='Julia09@gmail':
        st.sucess('email enviado com sucesso')
    else:
        st.error('email invalido')
    
