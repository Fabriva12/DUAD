from bubble_sort import bubble_sort

def test_bubble_sort_little_list_sort_correctly():
    # AAA
    # Arrange
    my_list = [4,2,77,66,55,8,3,67]
    # Act
    bubble_sort(my_list)
    # Assert
    assert my_list == sorted(my_list)


import random
def test_bubble_sort_big_list_sort_correctly():
    my_list2 = random.sample(range(200),100)
    bubble_sort(my_list2)
    assert my_list2 == sorted(my_list2)


def test_bubble_sort_empty_list_sort_correctly():
    my_list3 = []
    bubble_sort(my_list3)
    assert my_list3 == sorted(my_list3)

import pytest
def test_bubble_sort_wrong_parameter_dont_work():
    with pytest.raises(TypeError):
        my_list3 = ["Fernanda",3,"Joel","Melanny",5]
        bubble_sort(my_list3)