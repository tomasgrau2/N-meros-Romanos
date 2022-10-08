import unittest
import convert_decimal_to_roman

class TestDecimalToRoman(unittest.TestCase):

    def test_1(self):
        result = convert_decimal_to_roman.decimal_to_roman(4)
        self.assertEqual(result,"IV")
   
    def test_2(self):
        result = convert_decimal_to_roman.decimal_to_roman(9)
        self.assertEqual(result,"IX")

    def test_3(self):
        result = convert_decimal_to_roman.decimal_to_roman(40)
        self.assertEqual(result,"XL")

    def test_4(self):
        result = convert_decimal_to_roman.decimal_to_roman(90)
        self.assertEqual(result,"XC")

    def test_5(self):
        result = convert_decimal_to_roman.decimal_to_roman(400)
        self.assertEqual(result,"CD")

    def test_6(self):
        result = convert_decimal_to_roman.decimal_to_roman(900)
        self.assertEqual(result,"CM")

    def test_7(self):
        result = convert_decimal_to_roman.decimal_to_roman(1)
        self.assertEqual(result,"I")

    def test_8(self):
        result = convert_decimal_to_roman.decimal_to_roman(5)
        self.assertEqual(result,"V")

    def test_9(self):
        result = convert_decimal_to_roman.decimal_to_roman(10)
        self.assertEqual(result,"X")

    def test_10(self):
        result = convert_decimal_to_roman.decimal_to_roman(50)
        self.assertEqual(result,"L")

    def test_11(self):
        result = convert_decimal_to_roman.decimal_to_roman(100)
        self.assertEqual(result,"C")

    def test_12(self):
        result = convert_decimal_to_roman.decimal_to_roman(500)
        self.assertEqual(result,"D")

    def test_13(self):
        result = convert_decimal_to_roman.decimal_to_roman(1000)
        self.assertEqual(result,"M")    

if __name__ == "__main__":
        unittest.main()