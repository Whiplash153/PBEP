from task_fixtures import get_first

def test_sum(numbers):
    assert sum(numbers) == 6

def test_length(numbers):
    assert len(numbers) == 3

def test_first(new_numbers):
    assert get_first(new_numbers) == 1

def test_length(new_numbers):
    assert len(new_numbers) == 6