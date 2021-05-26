import pytest

class missed_wrong_entry(Exception):
    def __init__(self, message ="Unfilled or missed entry"):
        self.message = message
        super().__init__(self.message)

def test_check():
    a = 5
    b = 7
    c=a+b
    with pytest.raises(missed_wrong_entry):
         if c>10 :
                raise missed_wrong_entry
    