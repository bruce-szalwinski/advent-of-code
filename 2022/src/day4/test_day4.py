from day4 import assignments, to_set, is_superset


def test_assignments():

    actual = assignments()
    assert actual[0] == ["15-60", "14-59"]


def test_to_set():
    actual = to_set("15-60")
    assert actual == set(range(15, 60+1, 1))


def test_is_superset():
    # assert is_superset(to_set("2-8"), to_set("3-7")) is True
    # assert is_superset(to_set("2-4"), to_set("6-8")) is False
    # assert is_superset(to_set("5-7"), to_set("7-9")) is False
    assert is_superset(to_set("6-6"), to_set("4-6")) is True
    assert is_superset(to_set("64-64"), to_set("12-63")) is False

