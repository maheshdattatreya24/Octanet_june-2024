# 🏧 ATM Simulation System (Python)

## 👨‍💻 Developed By

* TENNETY MAHESH DATTATREYA

---

# 📌 Project Description

This project is a **simple ATM simulation system** implemented in Python. It allows users to perform basic banking operations such as checking balance, depositing money, withdrawing money, and viewing transaction history.

The system also includes **basic security features** like PIN authentication and limited login attempts.

---

# ⚙️ Features

* 🔐 PIN-based authentication (3 attempts limit)
* 💰 Check account balance
* 💸 Withdraw money
* 💵 Deposit money
* 📊 View transaction history
* ❌ Input validation (prevents invalid entries)
* 🚪 Exit option

---

# 🧠 System Workflow

1. User enters PIN
2. System validates PIN (max 3 attempts)
3. Displays ATM menu
4. User selects operation:

   * Balance check
   * Withdraw
   * Deposit
   * Transaction history
5. System processes request and updates balance
6. User can continue or exit

---

# 📁 Project Structure

```id="4m2w8n"
ATM_PROJECT/
│
├── atm.py
└── README.md
```

---

# ▶️ How to Run

## 🔹 Step 1: Install Python

Ensure Python 3.x is installed.

## 🔹 Step 2: Run the Program

```id="0k5g2z"
python atm.py
```

---

# 🔐 Default Credentials

```id="f1z5tw"
PIN: 2004
Initial Balance: ₹5000
```

---

# 📊 Sample Operations

* Check Balance → Displays current balance
* Withdraw → Deducts amount if sufficient funds
* Deposit → Adds amount to balance
* Transaction History → Shows all transactions

---

# ⚠️ Important Notes

* Only numeric inputs are accepted
* Withdrawal is not allowed if balance is insufficient
* Negative amounts are not accepted
* Account is blocked after 3 wrong PIN attempts

---

# 🎯 Future Improvements

* Add GUI (Tkinter / Streamlit)
* Support multiple user accounts
* Store data using files or database
* Hide PIN input for better security

---

# 📬 Conclusion

This project demonstrates basic **Python programming concepts**, including:

* Conditional statements
* Loops
* Exception handling
* Data structures (lists)

It serves as a beginner-friendly project for understanding real-world banking system logic.

---
