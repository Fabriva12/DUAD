from sum_list import sum_list
def test_sum_list_sum_all_elements_correct():
    # AAA
    # Arrange
    list_1 = [3,4,6,7]
    # Act
    result = sum_list(list_1)
    # Assert
    assert result == (20)


def test_sum_list_empty():
    list =[]
    result = sum_list(list)
    assert result == 0


def test_sum_list_wrong_elements():
    list = [3,4,6,7,"f",3,"r","t",3]
    try:
        result = sum_list(list)
        assert False, "Se esperaba TypeError pero no ocurrió"
    except TypeError:
        assert True