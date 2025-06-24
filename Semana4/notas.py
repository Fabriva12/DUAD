aprove_note= 0
desaprove_note= 0
notes = 0
average_aprove= 0
average_desaprove= 0
total_average=0
number_notes =0
notes_plus= 0
total_notes= int (input("Ingrese total de notas"))
while number_notes < total_notes:
    notes=int(input(f"Ingrese nota actual"))
    number_notes=number_notes+1
    notes_plus+=notes
    if notes < 70:
        desaprove_note=desaprove_note+1
        average_desaprove=average_desaprove+notes
    else:
        aprove_note +=1
        average_aprove=average_aprove+notes 
total_average=(notes_plus/total_notes)
if (aprove_note >0):
        average_aprove=average_aprove/aprove_note
if (desaprove_note>0):
    average_desaprove=average_desaprove/desaprove_note
print (f"la cantidad de notas aprobadas {aprove_note}")
print (f"el promedio de notas aprobadas {average_aprove}")
print (f"la cantidad de notas desaprobadas {desaprove_note}")
print (f"el promedio de desaprobadas {average_desaprove}")
print (f"el promedio total es {total_average}")