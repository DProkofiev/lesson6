import math


def test_filter():
    assert list(filter(lambda x: x % 2 == 0,
                       [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) == [2, 4, 6, 8, 0]


def test_map():
    assert list(map(str, [0, 2, 4, 6, 8])) == ['0', '2', '4', '6', '8']


def test_sorted():
    assert sorted([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_pi():
    assert round(math.pi, 2) == 3.14


def test_sqrt():
    assert math.sqrt(2) == 2 ** 0.5


def test_pow():
    assert math.pow(3, 3) == 3 ** 3


def test_hypot():
    assert math.hypot(2, 3) == math.sqrt(2 * 2 + 3 * 3)
