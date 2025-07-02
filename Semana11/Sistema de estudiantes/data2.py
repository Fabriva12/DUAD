import csv 
from actions2 import Student
def import_csv():
    total_student = []
    try:
        with open ("C:\\Users\\Usuario\\Desktop\\estudiantes.csv", "r", encoding= "utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = Student(
                row["student_name"],
                row["student_section"],
                row["spanish_note"],
                row["english_note"],
                row["social_est_note"],
                row["science_note"],
                row["average_note"]
            )
            total_student.append(student)
            return total_student
    except FileNotFoundError:
        print("No has creado un archivo csv previamente")


def export_csv(total_student):
    students_dicts = [student.to_dict() for student in total_student]
    with open("C:\\Users\\Usuario\\Desktop\\estudiantes.csv", "w", encoding="utf-8", newline='') as file:
        writer = csv.DictWriter(file, fieldnames = students_dicts[0].keys())
        writer.writeheader()
        for student in total_student:
            writer.writerows(students_dicts)
    print("Datos exportados exitosamente.")
