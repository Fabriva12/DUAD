my_list= ["perro", "hamster","gato", "pez"]
if len(my_list)>= 1:
    my_list[0], my_list[-1]=my_list[-1],my_list[0]
    print (f"{my_list}")