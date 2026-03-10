
import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import os
from datetime import datetime

# Import modules
import database
import analysis
import charts
import investment_analysis

# --- Configuração da Página --- #
st.set_page_config(layout="wide", page_title="Personal Finance Analyzer")
st.title("💰 Personal Finance Analyzer")

# --- Inicialização do Banco de Dados --- #
db_path = 'data/transactions.db'
if not os.path.exists('data'):
    os.makedirs('data')
database.init_db(db_path)

# --- Funções Auxiliares --- #
def get_all_transactions():
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM transactions ORDER BY date DESC", conn)
    conn.close()
    return df

def add_transaction_form():
    st.header("Adicionar Nova Transação")
    with st.form("transaction_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            date = st.date_input("Data", datetime.now())
            type_ = st.selectbox("Tipo", ["income", "expense"])
            amount = st.number_input("Valor", min_value=0.01, format="%.2f")
        with col2:
            category = st.text_input("Categoria")
            description = st.text_area("Descrição")
            fixed_expense = st.checkbox("Despesa Fixa?")

        submitted = st.form_submit_button("Adicionar Transação")
        if submitted:
            database.add_transaction(db_path, str(date), type_, amount, category, description, fixed_expense)
            st.success("Transação adicionada com sucesso!")

# --- Layout da Aplicação --- #
add_transaction_form()

st.sidebar.header("Navegação")
page = st.sidebar.radio("Ir para", ["Dashboard", "Histórico de Transações"])

if page == "Dashboard":
    st.header("Dashboard Financeiro")
    df = get_all_transactions()

    if not df.empty:
        # Estatísticas Financeiras
        st.subheader("Estatísticas Rápidas")
        total_balance, total_income, total_expense, avg_daily_expense, top_expense_category = analysis.get_financial_stats(df)
        st.write(f"**Saldo Atual:** R${total_balance:,.2f}")
        st.write(f"**Total de Receitas:** R${total_income:,.2f}")
        st.write(f"**Total de Despesas:** R${total_expense:,.2f}")
        st.write(f"**Média Diária de Gastos:** R${avg_daily_expense:,.2f}")
        st.write(f"**Maior Categoria de Gasto:** {top_expense_category}")

        # Gráficos
        st.subheader("Visualização de Gastos")
        col_charts_1, col_charts_2 = st.columns(2)
        with col_charts_1:
            st.pyplot(charts.plot_expenses_by_category(df))
        with col_charts_2:
            st.pyplot(charts.plot_income_vs_expense(df))
        st.pyplot(charts.plot_balance_over_time(df))

        # Insights Automáticos
        st.subheader("Insights Automáticos")
        insights = analysis.generate_insights(df)
        for insight in insights:
            st.info(insight)

        # Análise de Capacidade de Investimento
        st.subheader("Análise de Capacidade de Investimento")
        income_total, fixed_expenses, variable_expenses, monthly_leftover, investment_capacity = investment_analysis.calculate_investment_capacity(df)
        st.write(f"**Renda Total Mensal:** R${income_total:,.2f}")
        st.write(f"**Gastos Fixos Mensais:** R${fixed_expenses:,.2f}")
        st.write(f"**Gastos Variáveis Mensais:** R${variable_expenses:,.2f}")
        st.write(f"**Sobra Mensal:** R${monthly_leftover:,.2f}")
        st.write(f"**Capacidade de Investimento:** {investment_capacity:.2f}%")

        st.pyplot(investment_analysis.plot_financial_distribution(income_total, fixed_expenses, variable_expenses, monthly_leftover))

        recommendations = investment_analysis.generate_recommendations(investment_capacity, top_expense_category)
        for rec in recommendations:
            st.success(rec)

    else:
        st.info("Nenhuma transação registrada ainda. Adicione algumas transações para ver o dashboard.")

elif page == "Histórico de Transações":
    st.header("Histórico Completo de Transações")
    df = get_all_transactions()
    if not df.empty:
        st.dataframe(df)
    else:
        st.info("Nenhuma transação registrada ainda.")

