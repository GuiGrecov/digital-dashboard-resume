#1. importar bibliotecas

import pandas as pd
import yfinance as yf
import datetime as dt
import streamlit as st

st.set_page_config( page_title="INDICADORES FINANCEIROS", layout="wide")

st.title("INDICADORES DA BOLSA")
st.caption("Esse Dashboard foi gerado com enfoque para monitorar as ações BEST e algumas FIIs. Empresas de Bancos, Energia, Sustentabilidade e "
             "Telecomunicação")

# 2. Chamar a API
end_date = dt.datetime.today()
start_date =  dt.datetime(end_date.year-1,end_date.month,end_date.day)
lista_empresa = ["VALE3.SA", "ITSA4.SA", "PETR4.SA", "BBAS3.SA", "IRBR3.SA", "KLBN11.SA", "KNRI11.SA", "HGLG11.SA",
                 "SUZB3.SA", "UNIP6.SA", "TASA4.SA", "TRPL4.SA", "TAEE11.SA", "CMIG4.SA"]

with st.container():
    st.header("Insira as informações solicitadas")

    col1, col2, col3 = st.columns(3)

    with col1:
        ativo = st.selectbox("Selecione os ativo desejado:", options=lista_empresa)
    with col2:
        data_inicial = st.date_input("Selecione a Data inicial", start_date)
    with col3:
        data_final = st.date_input("Selecione a Data final", end_date)


#3. Gera o df
df = yf.download(tickers=ativo , start = data_inicial, end = data_final, actions=True)

# Preencha os valores NaN com zero (ou qualquer valor desejado)
df["Adj Close"].fillna(0, inplace=True)

if not df.empty:
    #4. Criando metricas
    ult_atualizacao = df.index.max() #Data da ultima att
    ult_cotacao = round(df.loc[df.index.max(), "Adj Close"], 2) #Pega a última cotacao
    menor_cotacao = round(df["Adj Close"].min(), 2) #Pega a menor cotacao do periodo
    maior_cotacao = round(df["Adj Close"].max(), 2) #Pega a maior cotacao do periodo
    prim_cotacao = round(df.loc[df.index.min(), "Adj Close"],2 ) #Pega a primeira cotacao encontrada
    delta = round(((ult_cotacao- prim_cotacao)/ prim_cotacao)*100,2) #A variacao da cotacao no periodo
    data = df[df["Dividends"]>0]
    dividendo = data["Dividends"].mean()
    dividendo_soma = data["Dividends"].sum()
    historico = data["Dividends"].count()
    Pl = ult_cotacao / dividendo_soma
    dividen_max = data["Dividends"].max()
    dividen_min = data["Dividends"].min()
    dividend_yeld = round(dividendo_soma/ult_cotacao,4)*100


    print(data)

    with st.container():

        st.subheader(f"Indicadores principais da ação {ativo}")
        col11, col12, col13, col14, col15 = st.columns(5)

        with col11:
            st.metric(f"Última atualização - {ult_atualizacao} "," R$ {:,.2f}".format(ult_cotacao),f"{delta}%" )

        with col12:
            st.metric(f"Menor cotação do período: "," R$ {:,.2f}".format(menor_cotacao))

        with col13:
            st.metric(f"Maior cotação do período: "," R$ {:,.2f}".format(maior_cotacao))

        with col14:
            st.metric(f"Preço/Lucro "," {:,.2f}".format(Pl))

        with col15:
            st.metric(f"Dividend yield","  {:,.2f} %".format(dividend_yeld) )


    with st.container():
        st.text("Preço das ações:")
        st.area_chart(df["Adj Close"])

        st.text("Mínimo, Preço das Ações e Máximo")
        st.line_chart(df[["Low","Adj Close", "High"]])

    with st.container():
        st.subheader("Sobre os dividendos")
        st.caption(f"Nessa parte iremos analisar profundamente a questão dos Dividendos pagos pela {ativo}")

        col5, col6, col7 = st.columns(3)

        with col5:
            st.caption("Tabela com todos os pagamentos no intervalo: ")
            st.dataframe(data[["Dividends"]])

        with col6:
            st.metric(f"Quantidade de pagamentos no intervalo: ", " {:,.2f}".format(historico))
            st.metric(f"Pagamento médio (Dividendos): ", " R$ {:,.2f}".format(dividendo))

        with col7:
            st.metric(f"Pagamento máximo Dividendo", "R$ {:,.2f}".format(dividen_max))
            st.metric(f"Pagamento mínimo Dividendo", "R$ {:,.2f}".format(dividen_min))


    with st.container():
        st.caption("Grafico de linhas com os pagamentos dos Dividendos:")
        st.line_chart(data["Dividends"])

    with st.container():
        st.subheader("Simulador de lucros com Dividendo")
        number = st.number_input('Quanto seria o investimento?')
        st.write('O investimento é de: R$ ', number)
        lucro = number * (dividend_yeld/100)
        compra = number / ult_cotacao
        print(compra)
        col21, col22 = st.columns(2)
        with col21:

            st.caption("FÓMULA PARA CÁLCULO DE LUCRO: Dividend Yield x Valor Investido")
            st.metric(f"O lucro médio seria de: ", " R$ {:,.2f}".format(lucro))

        with col22:
            st.caption("Para ter esse lucro médio precisaria a quantidade de ações abaixo")
            st.metric(f"Equivalente a ", " {:,.0f} Ações".format(compra))

else:
    st.warning("O DataFrame está vazio. Verifique se os dados foram carregados corretamente.")
