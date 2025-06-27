import csv 
def import_csv():
    try:
        with open ("C:\\Users\\Usuario\\Desktop\\estudiantes.csv", "r", encoding= "utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No has creado un archivo csv previamente")



def export_csv(total_student):
    header= ["Nombre", "Sección", "Nota de Español", "Nota de Inglés", "Nota de Sociales", "Nota de Ciencias", "Promedio"]
    with open("C:\\Users\\Usuario\\Desktop\\estudiantes.csv", "w", encoding="utf-8", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(total_student)
    print("Datos exportados exitosamente.")
