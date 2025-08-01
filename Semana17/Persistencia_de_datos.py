import csv
import os
from Clases import Movement, Category
def save_movement_csv(movement):
    fieldnames = ["category", "title", "type", "amount"]
    file_path = os.path.join("data", "movements.csv")
    os.makedirs("data", exist_ok=True)
    with open(file_path, "w", encoding="utf-8", newline='') as file:
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
    file_path = os.path.join("data", "movements.csv")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
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
    fieldname = ["name"]
    file_path = os.path.join("data", "category.csv")
    os.makedirs("data", exist_ok=True)
    with open(file_path, "w", encoding="utf-8", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldname)
        writer.writeheader()
        for cat in category:
            writer.writerow({"name": cat.name})


def charge_category_csv():
    category = []
    file_path = os.path.join("data", "category.csv")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                if row: 
                    category.append(Category(row[0]))
    except FileNotFoundError:
        print("No has creado un archivo CSV de categorías previamente.")
    return category