
import pandas as pd

def get_financial_stats(df):
    total_balance = df[df["type"] == "income"]["amount"].sum() - df[df["type"] == "expense"]["amount"].sum()
    total_income = df[df["type"] == "income"]["amount"].sum()
    total_expense = df[df["type"] == "expense"]["amount"].sum()

    # Calculate average daily expense
    if not df.empty:
        first_date = pd.to_datetime(df["date"]).min()
        last_date = pd.to_datetime(df["date"]).max()
        num_days = (last_date - first_date).days + 1
        if num_days == 0: # Handle case where there's only one day of data
            num_days = 1
        avg_daily_expense = df[df["type"] == "expense"]["amount"].sum() / num_days
    else:
        avg_daily_expense = 0

    # Top expense category
    expense_categories = df[df["type"] == "expense"].groupby("category")["amount"].sum()
    top_expense_category = expense_categories.idxmax() if not expense_categories.empty else "N/A"

    return total_balance, total_income, total_expense, avg_daily_expense, top_expense_category

def generate_insights(df):
    insights = []
    expense_df = df[df["type"] == "expense"]
    if not expense_df.empty:
        total_expenses = expense_df["amount"].sum()
        if total_expenses > 0:
            category_expenses = expense_df.groupby("category")["amount"].sum()
            for category, amount in category_expenses.items():
                percentage = (amount / total_expenses) * 100
                if percentage > 30: # Example threshold
                    insights.append(f"⚠️ **{category}** representa {percentage:.0f}% dos seus gastos totais.")
                    # Simple recommendation based on the insight
                    if percentage > 40:
                        insights.append(f"💡 Considere revisar seus gastos em **{category}** para otimizar seu orçamento.")
    return insights
