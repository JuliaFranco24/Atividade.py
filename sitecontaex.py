import streamlit as st
numero1=st.text_input('digite um número')
numero2=st.text_input('digite outro número')
if st.button('enviar'):

    resultado=int(numero1)+int(numero2)
    st.text(f'o resultado é {resultado}')