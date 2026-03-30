import pytest
from main import add
from task_parametrize import divide

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, -1, -2),
    (0, 0, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 2),
    (100, 10, 10),
    (10, 1, 10),
    (10, -1, -10)
])
def test_divide(a, b, expected):
    assert divide(a, b) == expected
