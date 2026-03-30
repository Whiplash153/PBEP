import pytest
from api_main import create_user, get_users, delete_user

def test_create_user(reset_users):
    user = create_user("Misha")

    assert user["name"] == "Misha"
    assert user["id"] == 1

def test_get_users(reset_users):
    create_user("A")
    create_user("B")

    users = get_users()

    assert len(users) == 2

@pytest.mark.parametrize("name", ["A", "B", "C"])
def test_multiply_users(reset_users, name):
    user = create_user(name)
    assert user["name"] == name

def test_delete_user(reset_users):
    user = create_user("A")

    delete_user(user["id"])
users = get_users()
assert len(users) == 0

