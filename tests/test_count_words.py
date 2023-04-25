from lib.count_words import *

def test_count_words_return_number():
    count_num_words = count_words("Hello")
    assert count_num_words == 5