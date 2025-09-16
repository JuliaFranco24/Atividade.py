import streamlit as st

st.sidebar.image('mylittlepony.jpg')
st.sidebar.title('calculo de IMC')

conls=st.columns(4)

conls[0].button('💕coluna 1')
conls[1].button('🦄coluna 2')
conls[2].button('✨coluna 3')
conls[3].button('🎀coluna 4')

if st.button('Botão inicial '):
    st.write('Você é um unicórnio! Bem-vindo ao clube dos chifrudos!🦄')

if st.button("Botão colorido"):
    st.write('Você é que nem a Rarity, com a sua generosidade!')
    st.image('rarity.jpg')