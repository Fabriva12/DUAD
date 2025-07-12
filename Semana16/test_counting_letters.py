from counting_letters import counting_letters
def test_counting_letters_upper_correct():
    my_sentence = ("HI IM FABRICIO")
    result = counting_letters(my_sentence)
    assert result ==(12,0)

def test_counting_letters_lower_correct():
    my_sentence = ("hi im fabricio")
    result = counting_letters(my_sentence)
    assert result ==(0,12)
    

def test_counting_letters_upper_and_lower_correct():
    my_sentence = ("Hi im Fabricio")
    result = counting_letters(my_sentence)
    assert result ==(2,10)