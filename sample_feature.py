def process_transactions(balance, transactions):
    history = []
    for t in transactions:
        action = t["action"]
        amount = t["amount"]
        # Fix for Bug 1: Reject negative amounts
        if isinstance(amount, (int, float)) and amount < 0:
            history.append(f"Error: Negative amount {amount} rejected")
            continue
        if action == "deposit":
            balance += amount
            history.append(f"Deposited {amount}, balance: {balance}")
        elif action == "withdraw":
            balance -= amount
            history.append(f"Withdrew {amount}, balance: {balance}")
        else:
            history.append("Unknown action")
    return balance, history
