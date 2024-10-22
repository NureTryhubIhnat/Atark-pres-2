# Extract Method

# До рефакторингу
def process_orders(orders):
    total = 0
    total_discount = 0

    for order in orders:
        if order['status'] == 'completed':
            total += order['amount']
        elif order['status'] == 'pending':
            discount = order['amount'] * 0.1
            # 10% знижка на невиконані замовлення

            total_discount += discount
            total += order['amount'] - discount

    print(f"Загальна сума: {total}, Знижка: {total_discount}")


orders = [
    {'status': 'completed', 'amount': 100},
    {'status': 'pending', 'amount': 200},
    {'status': 'completed', 'amount': 50},
]
process_orders(orders)

#
#
#
# Після рефакторингу


def process_orders(orders):
    total = 0
    total_discount = 0

    for order in orders:
        total += process_order(order)

    print(f"Загальна сума: {total}, Знижка: {total_discount}")


def process_order(order):
    if order['status'] == 'completed':
        return order['amount']
    elif order['status'] == 'pending':
        return apply_discount(order)
    return 0


def apply_discount(order):
    discount = order['amount'] * 0.1  # 10% знижка
    return order['amount'] - discount
