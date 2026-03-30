from main import add
from task import multiply

def test_add():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

def test_multiply_01():
    assert multiply(10, 6) == 60

def test_multiply_02():
    assert multiply(10, -10) == -100

def test_multiply_03():
    assert multiply(-1, -3) == 3