import pytest

@pytest.fixture
def numbers():
    return [1, 2, 3]

@pytest.fixture
def new_numbers():
    return [1, 2, 3, 4, 5, 6]