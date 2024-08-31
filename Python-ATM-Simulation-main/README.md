# ATM Machine Simulation

This project simulates the basic functions of an ATM machine including balance inquiry, cash withdrawal, cash deposit, PIN change, and transaction history.

## Features
- Account balance inquiry
- Cash withdrawal
- Cash deposit
- PIN change
- Transaction history

## Usage
```python
atm = ATM(pin=1234, balance=1000)
print(atm.balance_inquiry())
print(atm.cash_withdrawal(100))
print(atm.cash_deposit(200))
print(atm.change_pin(1234, 5678))
print(atm.get_transaction_history())
