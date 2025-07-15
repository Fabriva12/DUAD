from counting_letters import counting_upper_letters
def test_counting_letters_upper_correct():
    my_sentence = "HI IM FABRICIO"
    result = counting_upper_letters(my_sentence)
    assert result ==12

def test_counting_letters_upper_no_upper():
    my_sentence = "hi im fabricio"
    result = counting_upper_letters(my_sentence)
    assert result ==0



from counting_letters import counting_lower_letters
def test_counting_letters_lower_correct():
    my_sentence = "hi im fabricio"
    result = counting_lower_letters(my_sentence)
    assert result ==12
    

from counting_letters import total_letters
def test_counting_letters_upper_and_lower_correct():
    my_sentence = "Hi im Fabricio"
    result = total_letters(my_sentence)
    assert result ==12