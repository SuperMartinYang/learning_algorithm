import Roman_integer
import unittest

class FromRomanBadInput(unittest.TestCase):
    pattern = '''
    ^
    M{0,3}
    (CM | CD | D?C{0,3})    # 100 - 900
    (XC | XL | L?X{0,3})    # 10 - 90
    (IX | IV | V?I{0,3})    # 1 - 9
    $
    '''
    def test_malform_antecedent(self):
        '''from_roman should fail with malform antecedent, like'''
        for s in []:
            self.assertRaises(Roman_integer.InvalidRomanNumeralError, Roman_integer.from_roman, s)
    def test_too_many_repeated_numerals(self):
        '''from_roman should fail with '''
        for s in ['MMMM','DD','CCCC','LL','XXXX','VV','IIII']:
            self.assertRaises(Roman_integer.InvalidRomanNumeralError, Roman_integer.from_roman, s)
    def test_too_many_repeated_pairs(self):
        '''from_roman should fail with too many repeated pairs'''
        for s in ['CDCD','CMCM','XCXC',
                  'XLXL','IXIX','IVIV']:
            self.assertRaises(Roman_integer.InvalidRomanNumeralError, Roman_integer.from_roman, s)
    def test_none(self):
        '''to_roman should fail with empty string'''
        self.assertRaises(Roman_integer.InvalidRomanNumeralError, Roman_integer.from_roman, '')

if __name__ == '__main__':
    unittest.main()
