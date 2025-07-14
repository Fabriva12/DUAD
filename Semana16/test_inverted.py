from inverted import inverted_my_string
def test_inverted_string_correct():
    # AAA
    # Arrange
    my_string = "hola"
    # Act
    inverted = inverted_my_string(my_string)
    # Assert
    assert inverted == "aloh"


def test_inverted_string_empty():
    my_string = ""
    inverted = inverted_my_string(my_string)
    assert inverted == ""


def test_inverted_string_with_numbers():
    my_string = "I was born 25 years ago"
    inverted = inverted_my_string(my_string)
    assert inverted == "oga sraey 52 nrob saw I"
