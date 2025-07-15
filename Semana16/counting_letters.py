def counting_upper_letters(my_string):
    upper_letter = sum(1 for l in my_string if l.isupper())
    return upper_letter


def counting_lower_letters(my_string):
    lower_letter = sum(1 for l in my_string if l.islower())
    return lower_letter


def total_letters(my_string):
    total = counting_upper_letters(my_string) + counting_lower_letters(my_string)
    return total