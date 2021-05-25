import pytest

class missed_entry(Exception):
    def __init__(self, message ="Unfilled entry"):
        self.message = message
        super().__init__(self.message)

def test_check():
    a = 5
    b = 7
    c=a+b
    with pytest.raises(missed_entry):
         if c>10 :
                raise missed_entry
    