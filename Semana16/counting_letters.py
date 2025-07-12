def counting_letters(my_string):
    upper_letter = sum(1 for l in my_string if l.isupper())
    lower_letter = sum(1 for l in my_string if l.islower())
    return upper_letter, lower_letter
