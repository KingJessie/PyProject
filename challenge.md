This is a process feedback challenge. That means you should record yourself doing it and submit that recording to your coach for feedback. How do I do this?

Follow the design recipe to implement the following user story in your project:



1. Describe the Problem
As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.

2. Design the Function Signature
The signature of a function includes:

The name of the function.

def track_my_todo_tasks(text):
task = []
name = text (strings)
return string

pass


What parameters it takes, their names and data types.
name = task(string)
return string

What it returns and the data type of that value.
string 

Any other side effects it might have.
Steps 3 and 4 then operate as a cycle.
No

3. Create Examples as Tests

1. Checks if there is no tasks at the moment :
def test_is_task_empty():
result = track_my_todo_tasks(" ")
=> "Fail"

2. Check if the string  includes #TODO
text = " hello  I can't wait to check on my #TODO"
def test_includes_the_string_we_want():
result = track_my_todo_tasks(text)
=> "Pass"

2. Check if the string  start includes #
text = " hello  I can't wait to check on my #TODO"
def test_includes_the_string_we_want():
result = track_my_todo_tasks(text)
=> "Pass"

