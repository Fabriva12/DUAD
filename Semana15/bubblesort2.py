def bubble_sort_invert(my_list):
    for outer_index in range (len(my_list)-1):
        for index in range (len(my_list)-1,0,-1):
            current_element = my_list[index]
            next_element = my_list[index -1]
            if next_element > current_element:
                my_list[index] = next_element
                my_list[index -1] = current_element
    print(f"{my_list}")

my_list = [22,23,44,55,77,88,99,21,33]
bubble_sort_invert(my_list)