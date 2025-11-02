def process_transactions(balance, transactions):
    history = []
    for t in transactions:
        action = t.get("action")
        amount = t.get("amount")
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

if __name__ == "__main__":
    starting_balance = 50
    test_transactions = [
        {"action": "deposit", "amount": -20},        
        {"action": "withdraw", "amount": "thirty"},  
        {"action": "withdraw", "amount": 100},       
        {"action": "transfer", "amount": None},
        {"action": "deposit", "amount": 30},
        {"action": "withdraw", "amount": 10}
    ]
    final_balance, history = process_transactions(starting_balance, test_transactions)
    print("Transaction History:")
    for item in history:
        print(item)
    print("Final Balance:", final_balance)
