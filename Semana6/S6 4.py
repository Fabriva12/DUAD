def inverted_my_string():
    my_string= "sandwich de jamón"
    inverted= ""
    for index in range(len(my_string)-1,-1,-1):
        inverted += my_string[index]
    print (f"{inverted}")
    return inverted

inverted_my_string()
