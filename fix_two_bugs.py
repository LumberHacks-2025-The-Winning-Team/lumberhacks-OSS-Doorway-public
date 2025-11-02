def process_transactions(balance, transactions):
    history = []
    for t in transactions:
        action = t.get("action")
        amount = t.get("amount")
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            history.append(f"Error: Invalid amount {t['amount']}")
            continue
        if action == "withdraw":
            if amount > balance:
                history.append("Error: Overdraft not allowed")
                continue
            balance -= amount
            history.append(f"Withdrew {amount}, balance: {balance}")
        elif action == "deposit":
            balance += amount
            history.append(f"Deposited {amount}, balance: {balance}")
        elif action == "transfer":
            history.append(f"Transferred {amount}")
        else:
            history.append("Unknown action")
    return balance, history
