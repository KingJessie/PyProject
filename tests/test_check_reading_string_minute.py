from lib.check_reading_string_minute import *

#use does not give string:
def test_without_string():
  result = manage_my_time("")
  assert result == 0


  #Example 2
  #check the length of string
def test_is_this_a_string():
  result = manage_my_time("this")
  assert result == 0.005

def test_is_this_a_200_words():
  string = " ". join([ " Joan" for i in range(0,200)  ])
  result  = manage_my_time(string)

  assert result == 1.0
    
