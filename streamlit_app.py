import streamlit as st
#Colocar o nome do projeto!
st.set_page_config(page_title="Calculadora LEC", layout="wide")
st.title('Simulador do Lote Econômico de Compra')
st.markdown('---')
st.info('Fórmula: LEC = (2 * D * S/H)**1/2')
st.subheader('Insira os dados aqui:')
D = st.number_input('Demanda Atual (D):')
S = st.number_input('Custo do Pedido (S):')
H = st.number_input('Custo de Estocagem (H):')
if st.button('Calcular'):
  LEC = ( 2 * D * S / H)** (1/2)
  st.balloons()
  st.metric('O resultado é:', f'{LEC:.2f}')
