""" Unit test for roman.py """

import roman
import unittest

class Roman1ToTest(unittest.TestCase):

    def test_001_I(self):
        """ to_roman should convert 1 to "I" """
        self.__assertTranslatesToRoman(1, "I")

    def test_002_II(self):
        """ to_roman should convert 2 to "II" """
        self.__assertTranslatesToRoman(2, "II")

    def test_003_III(self):
        """ to_roman should convert 3 to "III" """
        self.__assertTranslatesToRoman(3, "III")

    def test_004_IV(self):
        """ to_roman should convert 4 to "IV" """
        self.__assertTranslatesToRoman(4, "IV")

    def test_005_V(self):
        """ to_roman should convert 5 to "V" """
        self.__assertTranslatesToRoman(5, "V")

    def test_006_IX(self):
        """ to_roman should convert 9 to "IX" """
        self.__assertTranslatesToRoman(9, "IX")

    def test_007_X(self):
        """ to_roman should convert 10 to "X" """
        self.__assertTranslatesToRoman(10, "X")

    def test_008_XL(self):
        """ to_roman should convert 40 to "XL" """
        self.__assertTranslatesToRoman(40, "XL")

    def test_009_L(self):
        """ to_roman should convert 50 to "L" """
        self.__assertTranslatesToRoman(50, "L")

    def test_010_XC(self):
        """ to_roman should convert 90 to "XC" """
        self.__assertTranslatesToRoman(90, "XC")

    def test_011_C(self):
        """ to_roman should convert 100 to "C" """
        self.__assertTranslatesToRoman(100, "C")

    def test_012_CD(self):
        """ to_roman should convert 400 to "CD" """
        self.__assertTranslatesToRoman(400, "CD")

    def test_013_D(self):
        """ to_roman should convert 500 to "D" """
        self.__assertTranslatesToRoman(500, "D")

    def test_014_CM(self):
        """ to_roman should convert 900 to "CM" """
        self.__assertTranslatesToRoman(900, "CM")

    def test_015_M(self):
        """ to_roman should convert 1000 to "M" """
        self.__assertTranslatesToRoman(1000, "M")

    def test_016_that_3999_is_the_upper_limit(self):
        """ to_roman should fail if the number is greater than 3999 """
        self.assertRaises(roman.OutOfRangeError,
                          roman.RomanNumeralConverter.to_roman,
                          4000)

    def test_017_that_0_is_the_lower_limit(self):
        """ to_roman should fail if the number is less than 1 """
        self.assertRaises(roman.OutOfRangeError,
                          roman.RomanNumeralConverter.to_roman,
                          0)
        self.assertRaises(roman.OutOfRangeError,
                          roman.RomanNumeralConverter.to_roman,
                          -22)

    def test_018_should_always_return_uppercase_letters(self):
        """ to_roman should always return uppercase roman numerals """
        result = roman.RomanNumeralConverter.to_roman(721)
        self.assertEqual(result, result.upper())

    def test_019_should_raise_an_exception_with_non_int_input(self):
        """ to_roman should fail if the input is not an int """
        self.assertRaises(roman.NotIntegerError,
                          roman.RomanNumeralConverter.to_roman,
                          0.5)
        self.assertRaises(roman.NotIntegerError,
                          roman.RomanNumeralConverter.to_roman,
                          "banana")

    def __assertTranslatesToRoman(self, integer, roman_numeral):
        result = roman.RomanNumeralConverter.to_roman(integer)
        self.assertEqual(roman_numeral, result)


class Roman2FromTest(unittest.TestCase):

    def test_017_1(self):
        """ from_roman should convert "I" to 1 """
        self.__assertTranslatesFromRoman("I", 1)

    def test_018_2(self):
        """ from_roman should convert "II" to 2 """
        self.__assertTranslatesFromRoman("II", 2)

    def test_019_3(self):
        """ from_roman should convert "III" to 3 """
        self.__assertTranslatesFromRoman("III", 3)

    def test_020_4(self):
        """ from_roman should convert "IV" to 4 """
        self.__assertTranslatesFromRoman("IV", 4)

    def test_021_5(self):
        """ from_roman should convert "V" to 5 """
        self.__assertTranslatesFromRoman("V", 5)

    def test_022_9(self):
        """ from_roman should convert "IX" to 9 """
        self.__assertTranslatesFromRoman("IX", 9)

    def test_023_10(self):
        """ from_roman should convert "X" to 10 """
        self.__assertTranslatesFromRoman("X", 10)

    def test_024_40(self):
        """ from_roman should convert "XL" to 40 """
        self.__assertTranslatesFromRoman("XL", 40)

    def test_025_50(self):
        """ from_roman should convert "L" to 50 """
        self.__assertTranslatesFromRoman("L", 50)

    def test_026_90(self):
        """ from_roman should convert "XC" to 90 """
        self.__assertTranslatesFromRoman("XC", 90)

    def test_027_100(self):
        """ from_roman should convert "C" to 100 """
        self.__assertTranslatesFromRoman("C", 100)

    def test_028_400(self):
        """ from_roman should convert "CD" to 400 """
        self.__assertTranslatesFromRoman("CD", 400)

    def test_029_500(self):
        """ from_roman should convert "D" to 500 """
        self.__assertTranslatesFromRoman("D", 500)

    def test_030_900(self):
        """ from_roman should convert "CM" to 900 """
        self.__assertTranslatesFromRoman("CM", 900)

    def test_031_1000(self):
        """ from_roman should convert "M" to 1000 """
        self.__assertTranslatesFromRoman("M", 1000)

    def test_032_too_many_repeated_numerals(self):
        """ from_roman should fail with too many repeated numerals """
        for number in ('MMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII'):
            self.assertRaises(roman.InvalidRomanNumeralError,
                              roman.RomanNumeralConverter.from_roman,
                              number)

    def test_033_too_many_repeated_pairs(self):
        """ from_roman should fail with too many repeated pairs """
        for number in ('CMCM', 'CDCD', 'XCXC', 'XLXL', 'IXIX', 'IVIV'):
            self.assertRaises(roman.InvalidRomanNumeralError,
                              roman.RomanNumeralConverter.from_roman,
                              number)

    def test_034_malformed_antecedent(self):
        """ from_roman should fail with a malformed antecedent """
        bad_numbers = (
            'IIMXCC',
            'VX',
            'DCM',
            'CMM',
            'IXIV',
            'MCMC',
            'XCX',
            'IVI',
            'LM',
            'LD',
            'LC'
        )

        for number in bad_numbers:
            self.assertRaises(roman.InvalidRomanNumeralError,
                              roman.RomanNumeralConverter.from_roman,
                              number)

    def __assertTranslatesFromRoman(self, roman_numeral, integer):
        result = roman.RomanNumeralConverter.from_roman(roman_numeral)
        self.assertEqual(integer, result)

if __name__ == "__main__":
    unittest.main()
