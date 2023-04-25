from lib.make_snippet import *

def test_takes_string_return_args():
    str_text = make_snippet("Bonjour")
    assert str_text == "Bonjour ..."