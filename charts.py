
import matplotlib.pyplot as plt
import pandas as pd

def plot_expenses_by_category(df):
    expense_df = df[df["type"] == "expense"]
    if expense_df.empty:
        fig, ax = plt.subplots()
        ax.text(0.5, 0.5, "Sem dados de despesas para exibir", horizontalalignment=\'center\', verticalalignment=\'center\', transform=ax.transAxes)
        ax.axis(\'off\')
        return fig

    category_expenses = expense_df.groupby("category")["amount"].sum()
    fig, ax = plt.subplots()
    ax.pie(category_expenses, labels=category_expenses.index, autopct=\"%1.1f%%\", startangle=90)
    ax.axis(\'equal\')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.set_title("Gastos por Categoria")
    return fig

def plot_income_vs_expense(df):
    income = df[df["type"] == "income"]["amount"].sum()
    expense = df[df["type"] == "expense"]["amount"].sum()

    if income == 0 and expense == 0:
        fig, ax = plt.subplots()
        ax.text(0.5, 0.5, "Sem dados de receitas/despesas para exibir", horizontalalignment=\'center\', verticalalignment=\'center\', transform=ax.transAxes)
        ax.axis(\'off\')
        return fig

    labels = ["Receitas", "Despesas"]
    values = [income, expense]

    fig, ax = plt.subplots()
    ax.bar(labels, values, color=["green", "red"])
    ax.set_title("Receitas vs Despesas")
    ax.set_ylabel("Valor (R$)")
    return fig

def plot_balance_over_time(df):
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values(by="date")
    df["cumulative_balance"] = df[df["type"] == "income"]["amount"].fillna(0) - df[df["type"] == "expense"]["amount"].fillna(0)
    df["cumulative_balance"] = df["cumulative_balance"].cumsum()

    if df.empty:
        fig, ax = plt.subplots()
        ax.text(0.5, 0.5, "Sem dados de saldo para exibir", horizontalalignment=\'center\', verticalalignment=\'center\', transform=ax.transAxes)
        ax.axis(\'off\')
        return fig

    fig, ax = plt.subplots()
    ax.plot(df["date"], df["cumulative_balance"], marker=\'o\')
    ax.set_title("Evolução do Saldo ao Longo do Tempo")
    ax.set_xlabel("Data")
    ax.set_ylabel("Saldo (R$)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig
