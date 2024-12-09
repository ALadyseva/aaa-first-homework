from one_hot_encoder import fit_transform
import pytest


def test_raise_error():
    with pytest.raises(TypeError):
        fit_transform()


def test_upper_low():
    assert fit_transform(['a', 'A']) == [('a', [0, 1]), ('A', [1, 0])]


def test_int():
    assert fit_transform([1, 2]) == [(1, [0, 1]), (2, [1, 0])]


def test_empty_string():
    assert fit_transform('') == [('', [1])]


if __name__ == '__main__':
    test_raise_error()
    test_upper_low()
    test_int()
    test_empty_string()
