import streamlit as st
lista=st.columns(4)

with lista[0]:
    st.write('coluna 1')
    st.button('clique aqui')

    nome=st.text_input('Digite seu nome')
    email=st.text_input('Digite seu email')

    st.write(nome)
    
with lista[1]:
    st.write('coluna2')
    st.button('toque aqui')
with lista[2]:
    st.write('coluna3')
    st.button('rele aqui')
with lista[3]:
    st.write('coluna4')
    st.button('click aqui')
