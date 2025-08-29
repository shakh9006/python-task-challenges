# Title: Compute User Order Statistics

# Description

"""
Your task is to aggregate statistics per user across all of their orders.

For each user, calculate:
total_spent – sum of price * qty for all items purchased by the user.
total_items – total number of items purchased (sum of all qty).
unique_products – the number of distinct product names purchased by the user.

"""

def orders_analytics(orders):
    result = {}
    for order in orders:
        uid = order['user_id']
        if uid not in result:
            result[uid] = {"user_id": uid, "total_spent": 0, "total_items": 0, "unique_products": set()}
        for it in order.get('items', []):
            result[uid]["total_spent"] += it.get('price', 0) * it.get('qty', 0)
            result[uid]["total_items"] += it.get('qty', 0)
            result[uid]["unique_products"].add(it.get('name'))

    out = []
    for uid, stats in result.items():
        out.append({
            "user_id": uid,
            "total_spent": stats["total_spent"],
            "total_items": stats["total_items"],
            "unique_products": len(stats["unique_products"])
        })
    return sorted(out, key=lambda x: x["user_id"])



orders_param = [
    {"order_id": 1, "user_id": "u1", "items": [{"name": "apple", "price": 2, "qty": 3}, {"name": "banana", "price": 1, "qty": 5}]},
    {"order_id": 2, "user_id": "u2", "items": [{"name": "apple", "price": 2, "qty": 1}, {"name": "pear", "price": 3, "qty": 2}]},
    {"order_id": 3, "user_id": "u1", "items": [{"name": "banana", "price": 1, "qty": 2}, {"name": "pear", "price": 3, "qty": 1}]},
    {"order_id": 4, "user_id": "u3", "items": [{"name": "apple", "price": 2, "qty": 10}]}
]
print(orders_analytics(orders_param))