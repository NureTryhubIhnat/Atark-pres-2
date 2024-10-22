# Inline Method

# Приклад коду до рефакторингу:

def calculate_discount(order):
    if order['status'] == 'pending':
        return order['amount'] * 0.1  # 10% знижка
    return 0


def process_orders(orders):
    total = 0
    total_discount = 0

    for order in orders:
        discount = calculate_discount(order)
        total_discount += discount
        total += order['amount'] - discount

    print(f"Загальна сума: {total}, Знижка: {total_discount}")


orders = [
    {'status': 'completed', 'amount': 100},
    {'status': 'pending', 'amount': 200},
]
process_orders(orders)


# Приклад коду після рефакторингу:

def process_orders(orders):
    total = 0
    total_discount = 0

    for order in orders:
        discount = order['amount'] * 0.1 if order['status'] == 'pending' else 0
        total_discount += discount
        total += order['amount'] - discount

    print(f"Загальна сума: {total}, Знижка: {total_discount}")
