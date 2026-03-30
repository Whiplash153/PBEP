import pytest
from api_main import users

@pytest.fixture
def reset_users():
    users.clear()