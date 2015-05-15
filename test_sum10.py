from sum_10 import sum10


def test_basic():
    ls = [5, 5]
    assert 5, 5 == sum10(ls)


def test_middle():
    ls = range(10)
    assert 4, 6 == sum10(ls)


def test_late():
    ls = [1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 7]
    assert 3, 7 == sum10(ls)
