from lib.capital_punctuation_char import *

#check if the string is empty:
def test_string_is_empty():
 result = verify_text_with_capital_letter_and_pm(" ")
 assert result == "Fail"


 #2.check if the string has capital letter:
def test_string_has_capital_at_the_start():
 result = verify_text_with_capital_letter_and_pm("Helloooooo")
 assert result == "close but not there yet!"

 #check if the string has capital letter at the start and ending punctuation mark:
def test_string_has_capital_at_the_start():
 result = verify_text_with_capital_letter_and_pm("Helloooooo!")
 assert result == "Pass"