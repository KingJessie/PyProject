'''Two
As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.
'''

2. Design the Function Signature
The signature of a function includes:

The name of the function. #done
What parameters it takes, their names and data types.
What it returns and the data type of that value.
Any other side effects it might have.

def verify_text_with_capital_letter_ and_pm():
parameters it takes --->  (eg name =text) and string.
What it returns ----> string (eg: "Hello!")
Any other side effects it might have ---> No
pass


3. Create Examples as Tests
These are examples of the function being called with particular arguments, and what the function should return in each situation.

For complex challenges you might want to come up with a list of examples first and then test-drive

1.check if the string is empty:
def test_string_is_empty():
 result = verify_text_with_capital_letter_ and_pm("")
 assert result == Fail

 2.check if the string has capital letter:
def test_string_has_capital_at_the_start():
 result = verify_text_with_capital_letter_ and_pm("Helloooooo")
 assert result == Pass

  3.check if the string has capital letter at the start and ending punctuation mark:
def test_string_has_capital_at_the_start():
 result = verify_text_with_capital_letter_ and_pm("Helloooooo!")
 assert result == Pass




