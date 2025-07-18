import csv
from Clases import Movement, Category
def save_movement_csv(movement):
    fieldnames = ["category", "title", "type", "amount"]
    with open("C:\\Users\\Usuario\\Desktop\\movement.csv", "w", encoding="utf-8", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for mov in movement:
            writer.writerow({
                "category": mov.category,
                "title": mov.title,
                "type": mov.type,
                "amount": mov.amount
            })


def charge_movements_csv():
    movements = []
    try:
        with open("C:\\Users\\Usuario\\Desktop\\movement.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                mov = Movement(
                    title=row["title"],
                    type=row["type"],
                    category=row["category"],
                    amount=float(row["amount"])
                )
                movements.append(mov)
    except FileNotFoundError:
        print("No has creado un archivo CSV de movimientos previamente.")
    return movements


def save_category_csv(category):
    fieldname = vars(category[0]).keys()
    with open("C:\\Users\\Usuario\\Desktop\\category.csv", "w", encoding="utf-8", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldname)
        writer.writeheader()
        for cat in category:
            writer.writerow(vars(cat))


def charge_category_csv():
    category = []
    try:
        with open("C:\\Users\\Usuario\\Desktop\\category.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                if row: 
                    category.append(Category(row[0]))
    except FileNotFoundError:
        print("No has creado un archivo CSV de categorías previamente.")
    return category