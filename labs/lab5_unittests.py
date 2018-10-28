try:
    from broken import *
except ImportError:
    print('Import error for broken.py')

try:
    from lab5 import *
except ImportError:
    print('Import error for lab5.py')

import unittest

# Unit tests for broken.py
class TestEvenLen(unittest.TestCase):

    errorMessage = "Given string {}, got {} instead of {}"

    def test_empty_string(self):
        s = ''
        expected = True

        result = even_len(s)

        self.assertTrue(result, self.errorMessage.format(s, result, expected))
    
    def test_single_char(self):
        s = 'j'
        expected = False

        result = even_len(s)

        self.assertTrue(result == expected, self.errorMessage.format(s, result, expected))

    def test_odd_length(self):
        s = '84s92j1'
        expected = False

        result = even_len(s)

        self.assertTrue(result == expected, self.errorMessage.format(s, result, expected))

    def test_even_length(self):
        s = '84s92j'
        expected = True

        result = even_len(s)

        self.assertTrue(result, self.errorMessage.format(s, result, expected))

class TestEveryOther(unittest.TestCase):

    errorMessage = "Given input {}, expected {} but got {}"

    def test_empty_string(self):
        s = ''
        expected = ''

        result = every_other(s)

        self.assertEqual(result, expected, self.errorMessage.format(s, expected, result))
    
    def test_single_char(self):
        s = 's'
        expected = 's'

        result = every_other(s)

        self.assertEqual(result, expected, self.errorMessage.format(s, expected, result))
    
    def test_even_length(self):
        s = '84s92jzl'
        expected = '8s2z'

        result = every_other(s)

        self.assertEqual(result, expected, self.errorMessage.format(s, expected, result))

    def test_odd_length(self):
        s = '1ka8dk2a9d'
        expected = '1ad29'

        result = every_other(s)

        self.assertEqual(result, expected, self.errorMessage.format(s, expected, result))

class TestIsVowel(unittest.TestCase):
    
    errorMessage = 'Given letter {}, expected {} but got {}'
    
    def test_not_vowel_uppercase(self):
        c = 'K'
        expected = False

        result = is_vowel(c)

        self.assertTrue(result == expected, self.errorMessage.format(c, expected, result))
    
    def test_not_vowel_lowercase(self):
        c = 'k'
        expected = False

        result = is_vowel(c)

        self.assertTrue(result == expected, self.errorMessage.format(c, expected, result))

    def test_is_vowel_uppercase(self):
        c = 'O'
        expected = True

        result = is_vowel(c)

        self.assertTrue(result, self.errorMessage.format(c, expected, result))
    
    def test_is_vowel_lowercase(self):
        c = 'o'
        expected = True

        result = is_vowel(c)

        self.assertTrue(result, self.errorMessage.format(c, expected, result))

class TestStutter(unittest.TestCase):
    
    errorMessage = 'Given string {} and k {}, expected {}, got {}'

    def test_empty_string(self):
        s = ''
        k = 20
        expected = ''

        result = stutter(s, k)

        self.assertEqual(result, expected, self.errorMessage.format(s, k, expected, result))

    def test_no_consonants(self):
        s = 'uou'
        k = 43
        expected = 'uou'

        result = stutter(s, k)

        self.assertEqual(result, expected, self.errorMessage.format(s, k, expected, result))

    def test_single_consonant(self):
        s = 'uwu'
        k = 4
        expected = 'uwwwwu'

        result = stutter(s, k)

        self.assertEqual(result, expected, self.errorMessage.format(s, k, expected, result))
    
    def test_multiple_consonants(self):
        s = 'boats'
        k = 3
        expected = 'bbboatttsss'

        result = stutter(s, k)

        self.assertEqual(result, expected, self.errorMessage.format(s, k, expected, result))

class TestAllTitleCase(unittest.TestCase):
    
    errorMessage = "Given list of strings {}, got {} but expected {}"

    def test_empty_list(self):
        strings = []
        expected = True

        result = all_title_case(strings)

        self.assertTrue(result, self.errorMessage.format(strings, result, expected))

    def test_empty_string(self):
        strings = ['']
        expected = False

        result = all_title_case(strings)

        self.assertTrue(result == expected, self.errorMessage.format(strings, result, expected))

    def test_single_entry_true(self):
        strings = ['David']
        expected = True

        result = all_title_case(strings)

        self.assertTrue(result, self.errorMessage.format(strings, result, expected))
    
    def test_multiple_entries_true(self):
        strings = ['David', 'Asdf', 'Lmzns']
        expected = True

        result = all_title_case(strings)

        self.assertTrue(result, self.errorMessage.format(strings, result, expected))

    def test_multiple_entries_false(self):
        strings = ['David', 'asdf', 'Lmzns']
        expected = False

        result = all_title_case(strings)

        self.assertTrue(result == expected, self.errorMessage.format(strings, result, expected))

# Unit tests for lab5.py
class TestRemoveLetter(unittest.TestCase):

    errorMessage = 'Given string {} and char {}, expected {} but got {}'

    def test_no_occurrence(self):
        s = 'test'
        letter = 'k'
        expected = s

        result = remove_letter(s, letter)

        self.assertEqual(result, expected, self.errorMessage.format(s, letter, expected, result))

    def test_one_occurrence(self):
        s = 'test'
        letter = 'e'
        expected = 'tst'

        result = remove_letter(s, letter)

        self.assertEqual(result, expected, self.errorMessage.format(s, letter, expected, result))

    def test_empty_string(self):
        s = ''
        letter = 'k'
        expected = s

        result = remove_letter(s, letter)

        self.assertEqual(result, expected, self.errorMessage.format(s, letter, expected, result))

class TestInterleave(unittest.TestCase):
    
    errorMessage = 'Given strings {}, {} expected {} got {}'

    def test_empty_strings(self):
        s1 = ''
        s2 = ''
        expected = ''

        result = interleave(s1, s2)

        self.assertEqual(result, expected, self.errorMessage.format(s1, s2, expected, result))

    def test_non_empty_strings(self):
        s1 = '1234'
        s2 = 'abcd'
        expected = '1a2b3c4d'

        result = interleave(s1, s2)

        self.assertEqual(result, expected, self.errorMessage.format(s1, s2, expected, result))

class TestSumPositive(unittest.TestCase):
    
    errorMessage = 'Given list {}, expected sum {} but got {}'

    def test_empty_list(self):
        numbers = []
        expected = 0

        result = sum_positive(numbers)

        self.assertEqual(result, expected, self.errorMessage.format(numbers, expected, result))

    def test_negative_numbers_only(self):
        numbers = [-12, -23, 0, -98]
        expected = 0

        result = sum_positive(numbers)

        self.assertEqual(result, expected, self.errorMessage.format(numbers, expected, result))
        
    def test_positive_and_negatives(self):
        numbers = [-12, 23, 0, 98]
        expected = 121

        result = sum_positive(numbers)

        self.assertEqual(result, expected, self.errorMessage.format(numbers, expected, result))

    def test_positives(self):
        numbers = [12, 23, 0, 98]
        expected = 133

        result = sum_positive(numbers)

        self.assertEqual(result, expected, self.errorMessage.format(numbers, expected, result))

class TestSumBig(unittest.TestCase):

    errorMessage = 'Given list {} and x = {} , expected sum {} but got {}'

    def test_empty_list(self):
        numbers = []
        x = 20
        expected = 0

        result = sum_big(numbers, x)

        self.assertEqual(result, expected, self.errorMessage.format(numbers, x, expected, result))

    def test_large_x(self):
        numbers = [20, -10, 8, 72]
        x = 100
        expected = 0

        result = sum_big(numbers, x)

        self.assertEqual(result, expected, self.errorMessage.format(numbers, x, expected, result))
    
    def test_negatives(self):
        numbers = [-20, -10, -8, -72]
        x = 100
        expected = 0

        result = sum_big(numbers, x)

        self.assertEqual(result, expected, self.errorMessage.format(numbers, x, expected, result))

    def test_with_positive_x(self):
        numbers = [20, 10, 8, 0, 72]
        x = 20
        expected = 72

        result = sum_big(numbers, x)

        self.assertEqual(result, expected, self.errorMessage.format(numbers, x, expected, result))
        
    def test_with_negative_x(self):
        numbers = [-20, -10, -8, -72]
        x = -10
        expected = -8

        result = sum_big(numbers, x)

        self.assertEqual(result, expected, self.errorMessage.format(numbers, x, expected, result))
    
    def test_positive_negatives_with_negative_x(self):
        numbers = [-20, 10, -8, 0, 72]
        x = -10
        expected = 74

        result = sum_big(numbers, x)

        self.assertEqual(result, expected, self.errorMessage.format(numbers, x, expected, result))

class TestFindPositive(unittest.TestCase):
    
    errorMessage = 'Given list {} expected {} but got {}'

    def test_empty_list(self):
        numbers = []
        expected = None

        result = find_positive(numbers)

        self.assertTrue(result is None, self.errorMessage.format(numbers, expected, result))

    def test_empty_list(self):
        numbers = []
        expected = None

        result = find_positive(numbers)

        self.assertTrue(result is None, self.errorMessage.format(numbers, expected, result))

    def test_all_negatives(self):
        numbers = [-1, -20, -81, -3]
        expected = None

        result = find_positive(numbers)

        self.assertTrue(result is None, self.errorMessage.format(numbers, expected, result))

    def test_all_positives(self):
        numbers = [1, 20, 81, 3]
        expected = 0

        result = find_positive(numbers)

        self.assertEqual(result, expected, self.errorMessage.format(numbers, expected, result))

    def test_mixed(self):
        numbers = [-1, 20, -81, 3]
        expected = 1

        result = find_positive(numbers)

        self.assertEqual(result, expected, self.errorMessage.format(numbers, expected, result))

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
