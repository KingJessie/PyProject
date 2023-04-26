from lib.track_my_todo_task import *


# Checks if there is no tasks at the moment :



# Check if the string  includes #TODO
text = " hello  I can't wait to check on my #TODO "

def test_includes_the_string_we_want():
  result = track_my_todo_tasks(text)
  assert result == "Pass"


# Check if word # at the start of string and capital letters pass
text = " hello  I can't wait to check on my ToDO "

def test_does_not_include_at_the_start():
  result = track_my_todo_tasks(text)
  assert result == "Fail"



