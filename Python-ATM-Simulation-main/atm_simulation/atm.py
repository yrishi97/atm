# atm.py

class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def balance_inquiry(self):
        return self.balance

    def cash_withdrawal(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        self.transaction_history.append(f"Withdrew {amount}")
        return self.balance

    def cash_deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited {amount}")
        return self.balance

    def change_pin(self, old_pin, new_pin):
        if self.pin == old_pin:
            self.pin = new_pin
            self.transaction_history.append("PIN changed")
            return "PIN changed successfully"
        else:
            return "Incorrect PIN"

    def get_transaction_history(self):
        return self.transaction_history
