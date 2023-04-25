

def verify_text_with_capital_letter_and_pm(text):
    if (text[0].isupper() ) and text.endswith("!") :
        return "Pass"
    elif text[-1] !=  "!" and text[0].isupper():
      return "close but not there yet!"
    elif text == " " :
        return "Fail"



    