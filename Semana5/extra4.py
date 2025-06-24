my_list=[23, 33, 45, 67, 87, 43, 97, 45, 34]
major= -999
second_major= -998
for number in my_list:
    if number > major:
        second_major = major
        major = number
    elif major > number > second_major:
        second_major = number
print(f"{second_major}")