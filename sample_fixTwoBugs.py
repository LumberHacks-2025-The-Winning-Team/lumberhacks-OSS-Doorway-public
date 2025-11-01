def process_transactions(balance, transactions):
    history = []
    for t in transactions:
        action = t["action"]
        amount = t["amount"]
        try:
            amount = float(amount)
        except (ValueError, TypeError):
            history.append(f"Error: Invalid amount {t['amount']}")
            continue
        if action == "deposit":
            balance += amount
            history.append(f"Deposited {amount}, balance: {balance}")
        elif action == "withdraw":
            if amount > balance:
                history.append("Error: Insufficient funds for withdrawal")
                continue
            balance -= amount
            history.append(f"Withdrew {amount}, balance: {balance}")
        else:
            history.append("Unknown action")
    return balance, history
