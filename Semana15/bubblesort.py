def bubble_sort(list_to_sort):
    for outer_index in range(0, len(list_to_sort)-1):
        swapped = False
        for index in range(0, len(list_to_sort)-1-outer_index):
            current_element = list_to_sort[index]
            next_element = list_to_sort[index +1]
            print (f" Iteracion {index} Elemento actual {current_element} Siguiente elemento {next_element}") 
            if current_element > next_element:
                print('El elemento actual es mayor al siguiente. Intercambiandolos...')
                list_to_sort[index] = next_element
                list_to_sort[index+1] = current_element
                swapped = True
        if not swapped:
            break
    print(f"{list_to_sort}")
my_list = [23,-23,55,32,11,-77,44,10]
bubble_sort(my_list)