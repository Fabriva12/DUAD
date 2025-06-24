user_list=[]
major=-99999
for index in range(10):
    new_number=int(input("ingrese un numero"))
    user_list.append(new_number)
    if new_number>major:
        major=new_number
print (f"{user_list} el mas alto fue {major}")