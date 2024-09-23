from myproj.service.user import UserRepo
from myproj.file_repo.file_reader_factory import JsonData, TextData
from decimal import Decimal
import unittest

import pytest


def test_not_correct_data_to_user():
    with pytest.raises(ValueError) as e:
        s = UserRepo('fake_user')
    assert str(e.value).startswith('Unsupported')


def test_data_convert_to_user_from_json(user_repo_from_json, expected_user_repo):
    users = user_repo_from_json.get_all_users()
    assert len(users) == 2
    assert users == expected_user_repo.get_all_users()

def test_data_convert_to_user_from_text(user_repo_from_text, expected_user_repo):
    users = user_repo_from_text.get_all_users()
    assert len(users) == 2
    assert users == expected_user_repo.get_all_users()


def test_data_convert_to_user_from_list(user_repo_from_list, expected_user_repo):
    users = user_repo_from_list.get_all_users()
    assert len(users) == 2
    assert users == expected_user_repo.get_all_users()


def test_find_by_id(user_repo_from_list):
    s1 = user_repo_from_list.find_by_id(1)
    assert s1.id_ == 1


def test_find_by_id_not_found(user_repo_from_list):
    with pytest.raises(KeyError) as e:
        s = user_repo_from_list.find_by_id(111)
    assert str(e.value) == "'User Not Found'"


def test_delete(user_repo_from_list):
    user_repo_from_list.delete(1)
    assert len(user_repo_from_list.get_all_users()) == 1
    with pytest.raises(KeyError) as e:
        user_repo_from_list.find_by_id(1)
    assert str(e.value) == "'User Not Found'"


def test_delete_not_found(user_repo_from_list):
    with pytest.raises(KeyError) as e:
        user_repo_from_list.delete(999)
    assert str(e.value) == "'User Not Found'"
