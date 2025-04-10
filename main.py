import json
import os
from datetime import datetime

DATA_DIR = "data"
EXPENSES_FILE = os.path.join(DATA_DIR, "expenses.json")
BUDGETS_FILE = os.path.join(DATA_DIR, "budgets.json")

def load_data(file):
    if not os.path.exists(file):
        return {}
    with open(file, "r") as f:
        return json.load(f)

def save_data(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=2)

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Transport, etc): ").title()
    amount = float(input("Enter amount: "))

    expenses = load_data(EXPENSES_FILE)
    expenses.setdefault(date, []).append({"category": category, "amount": amount})
    save_data(EXPENSES_FILE, expenses)

    budgets = load_data(BUDGETS_FILE)
    month = date[:7]
    total_spent = sum(
        exp["amount"]
        for d, exps in expenses.items()
        if d.startswith(month)
        for exp in exps if exp["category"] == category
    )

    budget = budgets.get(month, {}).get(category)
    if budget and total_spent > budget:
        print(f"⚠️ Alert: You’ve exceeded the budget for {category} in {month}!")

def set_budget():
    month = input("Enter month (YYYY-MM): ")
    category = input("Enter category: ").title()
    amount = float(input("Enter monthly budget amount: "))

    budgets = load_data(BUDGETS_FILE)
    budgets.setdefault(month, {})[category] = amount
    save_data(BUDGETS_FILE, budgets)
    print("✅ Budget set successfully.")

def view_monthly_report():
    month = input("Enter month (YYYY-MM): ")
    expenses = load_data(EXPENSES_FILE)
    budgets = load_data(BUDGETS_FILE).get(month, {})

    category_totals = {}
    for date, daily_expenses in expenses.items():
        if date.startswith(month):
            for expense in daily_expenses:
                category = expense["category"]
                category_totals[category] = category_totals.get(category, 0) + expense["amount"]

    print(f"\n📊 Monthly Report for {month}")
    print("-" * 40)
    total = 0
    for cat, amt in category_totals.items():
        budget = budgets.get(cat, "N/A")
        print(f"{cat:15} | Spent: ${amt:.2f} | Budget: ${budget}")
        total += amt
    print("-" * 40)
    print(f"Total Spending: ${total:.2f}\n")

def main_menu():
    os.makedirs(DATA_DIR, exist_ok=True)
    while True:
        print("=== Expense Tracker Menu ===")
        print("1. Add Expense")
        print("2. Set Monthly Budget")
        print("3. View Monthly Report")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            set_budget()
        elif choice == "3":
            view_monthly_report()
        elif choice == "4":
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
