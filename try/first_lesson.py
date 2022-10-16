import pytest


def my_sum(a,b):
    return int(a) + int(b)


def test_my_sum_positive():
    """ Валидное сложение """
    assert my_sum(5, 5) == 10

def test_my_summ_negative():
    """ Невалидное сложение """
    assert my_sum(5, 6) != 10
