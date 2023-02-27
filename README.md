# Dashboards com Streamlit (em Python) 

Esse dashboard foi criado para monitorar minhas acoes e gerar posiveis analises que me mostrem lucros! 

## 1. Quais bibliotecas foram utilizadas?

-> pandas para organizar e criar o dataframe, junto com manipulacao de dados
-> streamlit para gerar o Dashboard 
-> yfinance api do Yahoo para termos acesso em real-time os indicadores financeiros de cada acao 


## 2. Como funciona a biblioteca streamlit? 

Funciona por meio de comandas simples e intuitivo, junto com uma documentacao clara e de facil entendimento. 

Alguns dos comandos mais utilizados no codigo foram: 
a) st.title(): inserir um título principal
b) st.header() e st.subheader(): inserir cabeçalho
c) st.markdown(): inserir um markdown
d) st.dataframe() e st.write(): exibe o dataframe
e) st.columns([N]): insere o numero de colunas que gostariamos de criar
f) st.container(): funcao que seleciona um espaco
g) st.dateinput(): insere uma data para puxar a API
h) st.selectbox(): responsavel por armazenar as opcoes de acoes que temos disponiveis

Link para documentacao da linguagem: https://docs.streamlit.io/library/get-started/main-concepts

## 3. Objetivos do codigo?

Eu criei esse codigo com 3 finalidades:
1 - monitorar com uma ferramenta intuitiva e simples as acoes que eu invisto e monitorar alguns indicadores. 
2 - simular possiveis lucros caso eu invista algum dinheiro nas acoes 
3 - Estou cansado de depender de softwares de investimento (e sempre tive curiosidade do "por que?" cada um deles gera valores diferentes em relacao a P/L, Dividend Yield...) 


