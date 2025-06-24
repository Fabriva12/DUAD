def prime_number():
    my_list=[1, 2, 3, 4, 5, 6, 7, 33, 44, 55, 66, 77, 23, 34, 54]
    prime_list= []
    for number in my_list:
        if number > 1:
            square_root = int(number **0.5)+1  
            prime_number = True
            for i in range(2,square_root):
                if number % i == 0:
                    prime_number = False
                    break
            if prime_number == True:
                prime_list.append(number)
    print (f"{prime_list}")

prime_number()