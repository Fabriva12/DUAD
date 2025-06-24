my_list = [1, 2, 3, 4, 5, 5, 3, 5, 6, 8, 9, 7, 7]
new_list= []
for number in my_list:
    if number not in new_list:
        new_list.append(number)
print(f"{new_list}")