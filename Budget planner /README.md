# 💰 Budget Planner

A command-line personal finance tracker built in Python that helps you manage income, categorise expenses, set spending thresholds, and export reports.

---

## About

The Budget Planner lets users track their monthly income and expenses across predefined categories. It warns users when they exceed their own set spending limits and allows them to export a full report as a CSV file. Built as part of the CTIP152 module at STADIO Higher Education.

---

## Features

- **Income Tracking** — Set and update your monthly income
- **Expense Entry** — Add multiple expenses and assign each to a category
- **Spending Categories** — Food, Transport, Personal, Entertainment, Other
- **Category Thresholds** — Set a budget limit per category and receive warnings when exceeded
- **View Expenses** — See all expenses grouped by category with totals and a grand total
- **Balance Calculator** — Shows remaining balance after all expenses
- **Category Search** — Look up a specific category and its breakdown
- **CSV Report Generation** — Exports all expenses to `budget_report.csv`

---

## How to Run

```bash
python Budget_planner.py
```

---

## Menu Options

```
1. Add income
2. Add expenses
3. Set category thresholds
4. View expenses
5. Balance remaining
6. Search category
7. Generate report
8. Exit
```

---

## Sample Output

```
====== Budget planner =======
Your income: 15000.0
--- Category: Food ---
 - Groceries: R1200.00
 - Takeaways: R600.00

 Food total cost: R1800.00 ---
WARNING: Food expenses (R1800.00) exceed threshold (R1500.00)

Grand total: R4500.00
```

---

## Skills Demonstrated

- Dictionary and nested data structure manipulation
- File I/O with the `csv` module
- Input validation and error handling (`try/except`)
- Modular function design
- Menu-driven CLI application structure

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)

---

## Author

**Sandiso Thebe**
BIS Student @ STADIO Higher Education
[GitHub](https://github.com/sxnd11so) · [LinkedIn](https://linkedin.com/in/sandiso-thebe-2476aa394)
