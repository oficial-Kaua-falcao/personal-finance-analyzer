
import pandas as pd
import matplotlib.pyplot as plt

def calculate_investment_capacity(df):
    income_df = df[df["type"] == "income"]
    expense_df = df[df["type"] == "expense"]

    income_total = income_df["amount"].sum()
    fixed_expenses = expense_df[expense_df["fixed_expense"] == True]["amount"].sum()
    variable_expenses = expense_df[expense_df["fixed_expense"] == False]["amount"].sum()

    total_expenses = fixed_expenses + variable_expenses
    monthly_leftover = income_total - total_expenses

    if income_total > 0:
        investment_capacity = (monthly_leftover / income_total) * 100
    else:
        investment_capacity = 0.0

    return income_total, fixed_expenses, variable_expenses, monthly_leftover, investment_capacity

def generate_recommendations(investment_capacity, top_expense_category):
    recommendations = []
    if investment_capacity > 30:
        recommendations.append("🟢 Excelente capacidade de investimento. Continue assim!")
    elif 10 <= investment_capacity <= 30:
        recommendations.append("🟡 Capacidade moderada de investimento. Explore opções para otimizar seus gastos.")
        recommendations.append(f"💡 Sua maior categoria de gasto é **{top_expense_category}**. Pequenas reduções aqui podem fazer uma grande diferença.")
    else:
        recommendations.append("🔴 Capacidade baixa de investimento. Considere reduzir gastos variáveis para aumentar sua capacidade.")
        recommendations.append(f"💡 Sua maior categoria de gasto é **{top_expense_category}**. Focar em reduzir esses gastos pode ser um bom começo.")
    return recommendations

def plot_financial_distribution(income_total, fixed_expenses, variable_expenses, monthly_leftover):
    labels = ["Gastos Fixos", "Gastos Variáveis", "Valor Investível"]
    sizes = [fixed_expenses, variable_expenses, monthly_leftover]
    colors = ["#ff9999", "#66b3ff", "#99ff99"]

    # Remove negative or zero values from sizes and corresponding labels/colors
    filtered_data = [(l, s, c) for l, s, c in zip(labels, sizes, colors) if s > 0]
    if not filtered_data:
        fig, ax = plt.subplots()
        ax.text(0.5, 0.5, "Sem dados para exibir distribuição financeira", horizontalalignment=\'center\', verticalalignment=\'center\', transform=ax.transAxes)
        ax.axis(\'off\')
        return fig

    labels, sizes, colors = zip(*filtered_data)

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, autopct=\"%1.1f%%\", startangle=90)
    ax.axis(\'equal\')
    ax.set_title("Distribuição da Renda")
    return fig
