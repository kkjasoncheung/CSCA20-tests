import unittest
from e1 import *

errorMessage = 'Incorrect area calculated.'

class TestConstantFunction(unittest.TestCase):

    def test_happyPath(self):
        result = constant_function()
        expected = 0

        self.assertEqual(result, expected, "Doesn't return 0.")
    
class TestAreaSquare(unittest.TestCase):
    
    def test_integerLength(self):
        length = 54
        result = area_square(length)
        expected = length*length

        self.assertEqual(result, expected, errorMessage)

    def test_zeroLength(self):
        length = 0
        result = area_square(length)
        expected = length*length

        self.assertEqual(result, expected, errorMessage)

    def test_floatLength(self):
        length = 3.14
        result = area_square(length)
        expected = length*length

        self.assertAlmostEqual(result, expected, places = 7, msg=errorMessage, delta=0.0000001)


class TestAreaParallelogram(unittest.TestCase):
    
    def test_integerBaseHeight(self):
        base = 4
        height = 8

        result = area_parallelogram(base, height)
        expected = base * height

        self.assertEqual(result, expected, errorMessage)

    def test_integerBaseFloatHeight(self):
        base = 4
        height = 6.5234

        result = area_parallelogram(base, height)
        expected = base * height

        self.assertAlmostEqual(result, expected, places = 7, msg=errorMessage, delta=0.0000001)

    def test_floatBaseIntegerHeight(self):
        base = 4.3423
        height = 6

        result = area_parallelogram(base, height)
        expected = base * height

        self.assertAlmostEqual(result, expected, places = 7, msg=errorMessage, delta=0.0000001)

    def test_floatBaseHeight(self):
        base = 4.2390
        height = 3.124

        result = area_parallelogram(base, height)
        expected = base * height

        self.assertAlmostEqual(result, expected, places = 7, msg=errorMessage, delta=0.0000001)

    def test_zeroBaseNonZeroHeight(self):
        base = 0
        height = 1.123

        result = area_parallelogram(base, height)
        expected = base * height

        self.assertEqual(result, expected, errorMessage)  

    def test_zeroBaseHeight(self):
        base = 0
        height = 0

        result = area_parallelogram(base, height)
        expected = base * height

        self.assertEqual(result, expected, errorMessage)  


class TestIsStringEmpty(unittest.TestCase):
    
    stringEmptyError = 'Should not be empty'


    def test_first_function_no_print(self):
        self.assertFalse('print' in is_string_empty.__code__.co_names, 'You should return the result as a boolean instead of calling print()')

    def test_returnType(self):
        testString = ''
        result = is_string_empty(testString)
        isBoolean = isinstance(result, bool)
        self.assertTrue(isBoolean, 'The type of the return value is not a boolean.')

    def test_emptyString(self):
        testString = ''
        result = is_string_empty(testString)

        self.assertTrue(result, 'Should be empty')
        
    def test_whitespaceInString(self):
        testString = '  '
        result = is_string_empty(testString)

        self.assertFalse(result, self.stringEmptyError)
        
    def test_whitespaceAtBeginning(self):
        testString = ' ASDF'
        result = is_string_empty(testString)

        self.assertFalse(result, self.stringEmptyError)

    def test_whitespaceAtEnd(self):
        testString = 'ASDF   '
        result = is_string_empty(testString)

        self.assertFalse(result, self.stringEmptyError)

    def test_whitespaceInMiddle(self):
        testString = 'AS   DF'
        result = is_string_empty(testString)

        self.assertFalse(result, self.stringEmptyError)

    def test_whitespaceAround(self):
        testString = '  ASDF    '
        result = is_string_empty(testString)

        self.assertFalse(result, self.stringEmptyError)

    def test_whitespaceMiddleAndAround(self):
        testString = '    AS   DF '
        result = is_string_empty(testString)

        self.assertFalse(result, self.stringEmptyError)

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)