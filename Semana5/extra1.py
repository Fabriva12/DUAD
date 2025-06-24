list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pair_plus=0
for index in range(len(list)):
    if list[index] % 2 == 0:
        pair_plus += list[index]
print(f"{pair_plus}")