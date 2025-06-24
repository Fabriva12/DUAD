def sum_list(my_list):
    sum_number=0
    for number in my_list:
        sum_number += number
    return sum_number

my_list = [1, 2, 3, 4, 11, 22, 33, 44]
result = sum_list(my_list)
print(f"{result}")