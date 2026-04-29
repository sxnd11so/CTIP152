
# 📚 Digital Archive Portal

A command-line library management system built in Python, designed to help librarians register, log in, and manage a digital book inventory.

---

## About

The Digital Archive Portal simulates a basic library system where staff can register accounts, securely log in, and perform full CRUD operations on a book catalogue. Built as part of the CTIP152 module at STADIO Higher Education.

---

## Features

- **Librarian Registration** — Collects name, surname, staff ID, and password with validation rules
- **Staff Login** — Authenticates users with a 3-attempt lockout for security
- **Book Inventory Dashboard** — Full menu-driven system for managing books
  - Add single or multiple books with title length and ISBN validation
  - Auto-generate unique accession numbers per book
  - View all catalogued books
  - Search books by title
  - Delete books by title
  - Inventory report (Coming Soon)

---

## Validation Rules

| Field | Rule |
|-------|------|
| Staff ID | Must be 6 characters and contain a period (`.`) |
| Password | Minimum 10 characters, must include uppercase, digit, and an operator (`+`, `-`, `*`, `/`) |
| ISBN | Must be exactly 13 digits |
| Book Title | Maximum 30 characters |

---

## How to Run

```bash
# Run in Jupyter Notebook
jupyter notebook main.ipynb
```

> **Note:** This project uses `input()` and is designed to run in a terminal or Jupyter Notebook environment, not as a web app.

---

## Skills Demonstrated

- Dictionary and list manipulation
- Input validation with `while` loops
- Error handling with `try/except`
- Function decomposition and modular design
- Menu-driven CLI application structure

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)

---

## Author

**Sandiso Thebe**
BIS Student @ STADIO Higher Education
[GitHub](https://github.com/sxnd11so) · [LinkedIn](https://linkedin.com/in/sandiso-thebe-2476aa394)
