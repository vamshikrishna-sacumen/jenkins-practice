from source.main import *

def test_add():
    assert add(4,3) == 7
    assert add(1,2) != 4

def test_divide():
    assert divide(4,2) == 2
