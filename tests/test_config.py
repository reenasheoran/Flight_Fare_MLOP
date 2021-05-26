import pytest
from flask import request

class missed_wrong_entry(Exception):
    def __init__(self, message ="Unfilled or missed entry"):
        self.message = message
        super().__init__(self.message)

def test_check():
    Dep_Time=request.form["Dep_Time"]
    Arrival_Time = request.form["Arrival_Time"]
    with pytest.raises(ValueError):
         if Dep_Time==Arrival_Time :
                raise missed_wrong_entry
    