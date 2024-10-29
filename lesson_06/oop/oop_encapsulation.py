class BankAccount:
    def __init__(self, account_number: str, balance: float):
        self._account_number = account_number  # Protected attribute
        self.__balance = balance  # Private attribute

    # Getter for balance
    def get_balance(self) -> float:
        return self.__balance

    # Setter for balance
    def set_balance(self, amount: float):
        if amount >= 0:
            self.__balance = amount
        else:
            raise ValueError("Balance cannot be negative")

    # Method to deposit money
    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive")

    # Method to withdraw money
    def withdraw(self, amount: float):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount")


# יצירת אובייקט של BankAccount
account = BankAccount("123456789", 1000)

# # שימוש ב-getter לקבלת המאזן
print(account.get_balance())  # פלט: 1000

# שימוש ב-deposit וב-withdraw
account.deposit(500)  # פלט: Deposited 500. New balance: 1500
account.withdraw(200)  # פלט: Withdrew 200. New balance: 1300

# access to the protected member
print(f"{account._account_number = }")

# ניסיון לגשת ישירות ל-balance יגרום לשגיאה
# print(account.__balance)  # AttributeError

# Name Mangling - access to the private member
# print(f"{account._BankAccount__balance = }")

# שינוי המאזן דרך ה-setter
account.set_balance(2000)
print(account.get_balance())  # פלט: 2000

account.withdraw(100000)

# ניסיון לשים מאזן שלילי
# account.set_balance(-500)  # ValueError: Balance cannot be negative
