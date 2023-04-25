
# calculate word read per range of 200 words per minute
def manage_my_time(string):
    time = 200
    word = string.split()
    words = len(word)
    return  words / time
  

