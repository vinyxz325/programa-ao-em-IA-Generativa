import streamlit as st

st.caption('atribuição de notas dos alunos')

nota = st.number_input('digite a nota do aluno')

if st.button('verificar resultado'):
   if nota >= 7:
      st.write('aluno aprovado')
   else: 
      st.write('aluno reprovado')
    

