def process_transactions(balance, transactions):
    history = []
    for t in transactions:
        action = t["action"]
        amount = t["amount"]
        if action == "deposit":
            balance += amount
            history.append(f"Deposited {amount}, balance: {balance}")
        elif action == "withdraw":
            balance -= amount
            history.append(f"Withdrew {amount}, balance: {balance}")
        else:
            history.append("Unknown action")
    return balance, history

if __name__ == "__main__":
    test_transactions = [
        {"action": "deposit", "amount": 100},
        {"action": "withdraw", "amount": "fifty"},
        {"action": "withdraw", "amount": 50},
        {"action": "withdraw", "amount": 70},  # Overdraft!
        {"action": "deposit", "amount": -25}
    ]
    balance, history = process_transactions(0, test_transactions)
    for line in history:
        print(line)
    print("Final balance:", balance)
