import Roman_integer
import unittest

class ToRomanBadInput(unittest.TestCase):
    def test_too_large(self):
        '''to_roman should fail with large number'''
        self.assertRaises(Roman_integer.OutOfRangeError, Roman_integer.to_roman, 4000)

    def test_negative(self):
        '''to_roman should fail with negative'''
        self.assertRaises(Roman_integer.OutOfRangeError, Roman_integer.to_roman, -1)

    def test_non_integer(self):
        '''to_roman should fail with non_integer input'''
        self.assertRaises(Roman_integer.NotIntegerError, Roman_integer.to_roman, 0.5)

    def test_zero(self):
        '''to_roman should fail with zero'''
        self.assertRaises(Roman_integer.OutOfRangeError, Roman_integer.to_roman, 0)

    def test_none(self):
        '''to_roman should fail with empty string'''
        self.assertRaises(Roman_integer.OutOfRangeError, Roman_integer.to_roman, '')

if __name__ == '__main__':
    unittest.main()
