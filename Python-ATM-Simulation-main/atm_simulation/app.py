# app.py

from flask import Flask, render_template, request, redirect, url_for
from atm import ATM

app = Flask(__name__)

# Initialize the ATM instance with a default PIN and balance
atm = ATM(pin=1234, balance=1000)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        action = request.form['action']
        try:
            if action == 'balance_inquiry':
                message = f"Your balance is: {atm.balance_inquiry()}"
            elif action == 'cash_withdrawal':
                amount = int(request.form['amount'])
                message = atm.cash_withdrawal(amount)
            elif action == 'cash_deposit':
                amount = int(request.form['amount'])
                message = atm.cash_deposit(amount)
            elif action == 'change_pin':
                old_pin = int(request.form['old_pin'])
                new_pin = int(request.form['new_pin'])
                message = atm.change_pin(old_pin, new_pin)
            elif action == 'transaction_history':
                return redirect(url_for('transaction_history'))
        except ValueError:
            message = "Please enter valid numbers for amounts and PINs."
    return render_template('index.html', message=message)

@app.route('/transaction_history')
def transaction_history():
    transactions = atm.get_transaction_history()
    return render_template('transaction_history.html', transactions=transactions)

if __name__ == "__main__":
    app.run(debug=True)
