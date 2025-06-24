sales = [
    {
        'date': '01/03/23',
        'customer_email': 'alice@gmail.com',
        'items': [
            {'name': 'Book', 'upc': 'ITEM-100', 'unit_price': 15.00},
            {'name': 'Pen', 'upc': 'ITEM-101', 'unit_price': 1.50},
        ],
    },
    {
        'date': '01/03/23',
        'customer_email': 'bob@yahoo.com',
        'items': [
            {'name': 'Notebook', 'upc': 'ITEM-102', 'unit_price': 7.25},
        ],
    },
    {
        'date': '02/03/23',
        'customer_email': 'alice@gmail.com',
        'items': [
            {'name': 'Backpack', 'upc': 'ITEM-103', 'unit_price': 29.99},
        ],
    },
]
total_pay={}
for sale in sales:
    email = sale["customer_email"]
    for item in sale["items"]:
        pay= item["unit_price"]
        if email in total_pay:
            total_pay[email] += pay
        else:
            total_pay[email]= pay
print (f"{total_pay}")