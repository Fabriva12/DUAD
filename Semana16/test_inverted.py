from inverted import inverted_my_string
def test_inverted_string_correct():
    # AAA
    # Arrange
    my_string = ("hola")
    # Act
    inverted = inverted_my_string(my_string)
    # Assert
    assert inverted == ("aloh")