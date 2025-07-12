from sum_list import sum_list
def test_sum_list_sum_all_elements_correct():
    # AAA
    # Arrange
    list_1 = (3,4,6,7)
    # Act
    result = sum_list(list_1)
    # Assert
    assert result == (20)