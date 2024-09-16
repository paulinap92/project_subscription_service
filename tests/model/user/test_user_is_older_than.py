from myproj.model.user import User, Destination
from datetime import date
import pytest



def test_get_id():
    u1 = User('Jan', 'Nowak', Destination.IC, date(2050, 11, 1),123)
    assert u1.get_id() == 123


def test_age_range():
    with pytest.raises(ValueError) as err:
        u1 = User('Jan', 'Nowak', Destination.IC, date(2050, 11, 1)).is_older_than(-1)

    assert "Age value not correct" == str(err.value)

def test_user_is_older_than():
    u1 = User('Jan', 'Nowak', Destination.IB, date(2000, 11, 1))
    assert u1.is_older_than(18)

def test_user_is_not_older_than():
    u1 = User('Jan', 'Nowak', Destination.PN, date.today())
    assert not u1.is_older_than(18)