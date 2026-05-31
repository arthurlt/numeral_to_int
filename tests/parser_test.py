import pytest

from numeral_to_int.parser import parse


def test_single_numeral():
    assert parse("I") == 1
    assert parse("V") == 5
    assert parse("X") == 10
    assert parse("L") == 50
    assert parse("C") == 100
    assert parse("D") == 500
    assert parse("M") == 1000


def test_two():
    assert parse("II") == 2


def test_three():
    assert parse("III") == 3


def test_four():
    assert parse("IV") == 4


def test_eight():
    assert parse("VIII") == 8


def test_fourteen():
    assert parse("XIV") == 14


def test_thirty():
    assert parse("XXX") == 30


def test_thirty_eight():
    assert parse("XXXVIII") == 38


def test_forty_two():
    assert parse("XLII") == 42


def test_nine_hundred():
    assert parse("CM") == 900


def test_nineteen_nity_eight():
    assert parse("MCMXCVIII") == 1998


def test_lowercase():
    assert parse("lxxxix") == 89
    assert parse("xcix") == 99
    assert parse("mm") == 2000


def test_invalid():
    with pytest.raises(ValueError):
        parse("foo")
