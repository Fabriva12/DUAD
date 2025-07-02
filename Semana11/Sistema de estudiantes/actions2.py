class Student:
    def __init__(self, student_name, student_section, spanish_note, english_note, social_est_note, science_note, average_note):
        self.student_name = student_name
        self.student_section = student_section
        self.spanish_note = spanish_note
        self.english_note = english_note
        self.social_est_note = social_est_note
        self.science_note = science_note
        self.average_note = average_note
    
    def to_dict(self):
        return {
            "student_name": self.student_name,
            "student_section": self.student_section,
            "spanish_note": self.spanish_note,
            "english_note": self.english_note,
            "social_est_note": self.social_est_note,
            "science_note": self.science_note,
            "average_note": self.average_note,
        }    

def create_student():
    total_student=[]
    while True:
        student= input("Quieres agregar un nuevo estudiante (si) (no)\n")
        if student == "si":
            student_name = input("Cual es el nombre del estudiante\n")
            student_section = input ("Cual es la seccion del estudiante\n")
            while True:
                try: 
                    spanish_note = int(input("Cual es la nota de español\n"))
                    if 0 <= spanish_note <=100:
                        break
                    else :
                        print("No ingresaste una nota entre 0 y 100")
                except ValueError:
                    print("no ingreso una nota valida")
            
            while True:
                try: 
                    english_note = int(input("Cual es la nota de inglés\n"))
                    if 0 <= english_note <=100:
                        break
                    else :
                        print("No ingresaste una nota entre 0 y 100")
                except ValueError:
                    print("no ingreso una nota valida")
            while True:
                try: 
                    social_est_note = int(input("Cual es la nota de sociales\n"))
                    if 0 <= social_est_note <=100:
                        break
                    else :
                        print("No ingresaste una nota entre 0 y 100")
                except ValueError:
                    print("no ingreso una nota valida")
            while True:
                try: 
                    science_note = int(input("Cual es la nota de ciencias\n"))
                    if 0 <= science_note <=100:
                        break
                    else :
                        print("No ingresaste una nota entre 0 y 100")
                except ValueError:
                    print("no ingreso una nota valida")
            average_note = (spanish_note + english_note + social_est_note + science_note)/4
            
            total_student.append(Student(student_name, student_section, spanish_note, english_note, social_est_note, science_note, average_note))
        elif student == "no":
            break
    return total_student


def show_new_student(total_student):
    for l in total_student:
        print(l.to_dict())

def average_3(total_student):
    average_order = sorted(total_student, key=lambda x : x.average_note, reverse= True)
    top_3 = average_order[:3]
    for student in top_3:
        print(f"{student.student_name} - Promedio: {student.average_note}")


def total_average(total_student):
    total = sum(l.average_note for l in total_student)
    average_total = total / len(total_student)
    print(f" Promedio general de todos los estudiantes: {average_total}")
