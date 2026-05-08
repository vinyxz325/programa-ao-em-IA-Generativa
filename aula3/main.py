import streamlit as st

st.caption('CADASTRO SIMPLES')


nome = st.text_input('nome:')
idade = st.number_input('idade:')
email = st.text_input ('email:')
altura = st.number_input ('altura:')

if st.button('cadastrar'):
    st.success('pessoa cadastrada')
#------------------------------------------------------

st.caption('TABUADA')

numero = st.number_input('numero:')

for x in range (0,11):
    calculo = x * numero
    st.write(f'{x} X {numero} = {calculo}')


