import unittest
from lab4 import *

class TestCountLetter(unittest.TestCase):
    
    errorMessage = "Incorrect number of occurrences for {} in {}"

    def test_multiple_occurrences(self):
        string = 'hippopotamus'
        ch = 'p'
        expected = 3

        result = count_letter(string, ch)

        self.assertEqual(result, expected, self.errorMessage.format(ch, string))
    
    def test_zero_occurrences(self):
        string = 'hippopotamus'
        ch = 'z'
        expected = 0
        
        result = count_letter(string, ch)

        self.assertEqual(result, expected, self.errorMessage.format(ch, string))

    def test_uppercase(self):
        string = 'hiPPopotamus'
        ch = 'p'
        expected = 1

        result = count_letter(string, ch)

        self.assertEqual(result, expected, self.errorMessage.format(ch, string))

class TestRemoveDigits(unittest.TestCase):

    errorMessage = "Incorrect string returned for {}"

    def test_multiple_digits(self):
        string = 'a84jd931sd1'
        expected = 'ajdsd'

        result = remove_digits(string)

        self.assertEqual(result, expected, self.errorMessage.format(string))

    def test_no_digits(self):
        string = 'ajdsd'
        expected = string

        result = remove_digits(string)

        self.assertEqual(result, expected, self.errorMessage.format(string))

    def test_only_digits(self):
        string = '1294'
        expected = ''

        result = remove_digits(string)

        self.assertEqual(result, expected, self.errorMessage.format(string))

class TestRepeatCharacter(unittest.TestCase):
    
    errorMessage = "Incorrect string returned for a string {} and ch {}"

    def test_multiple_occurrences(self):
        string = 'hippopotamus'
        ch = 'p'
        expected = 'ppp'

        result = repeat_character(string, ch)

        self.assertEqual(result, expected, self.errorMessage.format(string, ch))
    
    def test_zero_occurrences(self):
        string = 'hippopotamus'
        ch = 'z'
        expected = ''
        
        result = repeat_character(string, ch)

        self.assertEqual(result, expected, self.errorMessage.format(string, ch))

    def test_uppercase(self):
        string = 'hiPPopotamus'
        ch = 'p'
        expected = 'p'

        result = repeat_character(string, ch)

        self.assertEqual(result, expected, self.errorMessage.format(string, ch))

class TestEveryThird(unittest.TestCase):
    """
    These test cases are slightly modified to check if the returned list has ~1/3
    the length of the original list +/- 1.
    """
    errorMessage = "Incorrect number of elements returned for list {}"

    def test_empty_list(self):
        list = []
        expected = 0

        result_length = len(every_third(list))
        result = result_length == expected
        
        self.assertTrue(result, self.errorMessage.format(list))

    def test_multiple_of_three(self):
        list = ['a', 'b', 'c', 'd', 'e', 'f']
        expected_0 = 2
        expected_1 = 3

        result_length = len(every_third(list))
        result = (result_length == expected_0) or (result_length == expected_1)

        self.assertTrue(result, self.errorMessage.format(list))

    def test_small_lists(self):
        list = ['a', 'b']
        expected = 1
        
        result_length = len(every_third(list))
        result = result_length == expected
        
        self.assertTrue(result, self.errorMessage.format(list))

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)

