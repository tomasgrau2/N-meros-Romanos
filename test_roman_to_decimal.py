import unittest
import convert_roman_to_decimal

class RomantoDecimal(unittest.TestCase):

    def test_1(self):
        self.assertEqual(convert_roman_to_decimal.roman_to_decimal("I"),1)

    def test_2(self):
        self.assertEqual(convert_roman_to_decimal.roman_to_decimal("II"),2)

    def test_3(self):
        self.assertEqual(convert_roman_to_decimal.roman_to_decimal("IV"),4)

    def test_4(self):
        self.assertEqual(convert_roman_to_decimal.roman_to_decimal("V"),5)

    def test_5(self):
        self.assertEqual(convert_roman_to_decimal.roman_to_decimal("X"),10)

    def test_6(self):
        self.assertEqual(convert_roman_to_decimal.roman_to_decimal("XV"),15)

    def test_7(self):
        self.assertEqual(convert_roman_to_decimal.roman_to_decimal("XL"),40)

    def test_8(self):
        self.assertEqual(convert_roman_to_decimal.roman_to_decimal("L"),50)

    def test_9(self):
        self.assertEqual(convert_roman_to_decimal.roman_to_decimal("XC"),90)

    def test_10(self):
        self.assertEqual(convert_roman_to_decimal.roman_to_decimal("CV"),105)

    def test_11(self):
        self.assertEqual(convert_roman_to_decimal.roman_to_decimal("DCLVIII"),658)

    def test_12(self):
        self.assertEqual(convert_roman_to_decimal.roman_to_decimal("CMLVI"),956)

    def test_13(self):
        self.assertEqual(convert_roman_to_decimal.roman_to_decimal("MDCXLIII"),1643)

    def test_14(self):
        self.assertEqual(convert_roman_to_decimal.roman_to_decimal("MMCDXXXII"),2432)

    def test_15(self):
        self.assertEqual(convert_roman_to_decimal.roman_to_decimal("MMM"),3000)

if __name__ == '__main__':
    unittest.main()
