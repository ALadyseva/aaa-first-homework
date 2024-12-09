from one_hot_encoder import fit_transform
import unittest


class TestFitTransform(unittest.TestCase):
    def test_int(self):
        actual = fit_transform([1, 2])
        expected = [(1, [0, 1]), (2, [1, 0])]
        self.assertEqual(actual, expected)

    def test_empty_string(self):
        self.assertEqual(fit_transform(''), [('', [1])])
        self.assertNotEqual(fit_transform(''), [])

    def test_raise_error(self):
        with self.assertRaises(TypeError):
            fit_transform()

    def test_upper_low(self):
        self.assertTrue(fit_transform(['a', 'A']) != fit_transform(['a', 'a']))


if __name__ == '__main__':
    testing = TestFitTransform()
    testing.test_int
    testing.test_empty_string
    testing.test_raise_error
    testing.test_upper_low
