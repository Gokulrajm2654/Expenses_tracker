# 💰 Expense Tracker Application

A simple Python command-line application to help users track daily expenses and manage monthly savings goals with budget alerts.

---

## ✨ Features

- ✅ Log daily expenses
- 📂 Categorize expenses (e.g., Food, Transport, Entertainment)
- 💵 Set monthly budgets per category
- 🚨 Get alerts when exceeding category budgets
- 📊 Generate monthly spending reports
- 🧾 Compare actual spending vs. budget

---

## 🛠 Requirements

- Python 3.x
- No external libraries required (standard library only)

---

## 🚀 How to Run

1. **Clone the repository or download the files**
2. Open a terminal and navigate to the `expense_tracker/` directory.
3. Create the data folder (if it doesn’t exist):
    ```bash
    mkdir data
    ```
4. Run the app:
    ```bash
    python main.py
    ```

---

## 📋 Usage Guide

### Main Menu Options:
1. **Add Expense**  
   - Enter the date, category, and amount spent.
   - Automatically checks and warns if budget is exceeded.

2. **Set Monthly Budget**  
   - Specify a month (`YYYY-MM`), category, and the budget amount.

3. **View Monthly Report**  
   - Shows total and category-wise spending.
   - Compares actual spending to the budget set.

4. **Exit**  
   - Quits the application.

---

## 🔧 Example Categories

- Food  
- Transport  
- Entertainment  
- Utilities  
- Health  
- Miscellaneous

> You can add your own custom categories as needed.

---

## 📈 Future Improvements (Suggestions)

- CSV or Excel export of reports  
- Data visualization using Matplotlib  
- GUI with Tkinter or PyQt  
- Support for multiple users with login system  
- Database integration (SQLite, PostgreSQL)

---

## 📝 License

This project is open-source and free to use. Customize it to your needs!

---
