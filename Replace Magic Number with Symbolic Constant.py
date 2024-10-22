# Replace Magic Number with Symbolic Constant

# Приклад коду до рефакторингу:
def process_orders(orders):
    total = 0
    total_discount = 0

    for order in orders:
        discount = order['amount'] * \
            0.1 if order['status'] == 'pending' else 0  # магічне число
        total_discount += discount
        total += order['amount'] - discount

    print(f"Загальна сума: {total}, Знижка: {total_discount}")


# Приклад коду після рефакторингу:

PENDING_DISCOUNT_RATE = 0.1  # символічна константа


def process_orders(orders):
    total = 0
    total_discount = 0

    for order in orders:
        discount = order['amount'] * \
            PENDING_DISCOUNT_RATE if order['status'] == 'pending' else 0
        total_discount += discount
        total += order['amount'] - discount

    print(f"Загальна сума: {total}, Знижка: {total_discount}")
