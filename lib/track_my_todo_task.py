
def track_my_todo_tasks(text):
  split_text = text.split(" ")
  for char in split_text:
    if char in "#TODO" and char.isupper():
      return "Pass"
    elif char == "TODO" and char == "#Todo":
      return "Fail"

  













