def process_transactions(balance, transactions):
    history = []
    for t in transactions:
        action = t.get("action")
        amount = t.get("amount")
        if isinstance(amount, (int, float)) and amount < 0:
            history.append(f"Error: Negative amount {amount} not allowed")
            continue
        if action == "deposit":
            balance += amount
            history.append(f"Deposited {amount}, balance: {balance}")
        elif action == "withdraw":
            balance -= amount
            history.append(f"Withdrew {amount}, balance: {balance}")
        elif action == "transfer":
            history.append(f"Transferred {amount}")
        else:
            history.append("Unknown action")
    return balance, history
