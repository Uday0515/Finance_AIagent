import os
from dotenv import load_dotenv

load_dotenv()

def get_user_input():
    print("Finance AI Agent")
    print("-" * 30)
    income = float(input("Enter monthly income: "))
    expenses = {}
    categories = ["rent", "food", "transport", "shopping", "utilities"]
    print("\nEnter monthly expenses:")
    for cat in categories:
        value = input(f"  {cat}: ")
        if value:
            expenses[cat] = float(value)
    return {"monthly_income": income, "expenses": expenses}

def analyze_budget(data):
    print("\nBudget Analysis")
    print("-" * 30)
    total = sum(data["expenses"].values())
    savings = data["monthly_income"] - total
    print(f"Income   : {data['monthly_income']:,.0f}")
    print(f"Expenses : {total:,.0f}")
    print(f"Savings  : {savings:,.0f}")

def main():
    data = get_user_input()
    analyze_budget(data)

if __name__ == "__main__":
    main()