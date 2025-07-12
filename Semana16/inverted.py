def inverted_my_string(my_string):
    inverted= ""
    for index in range(len(my_string)-1,-1,-1):
        inverted += my_string[index]
    return inverted


