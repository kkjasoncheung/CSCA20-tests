import unittest
from e3 import *

# Unit Tests: ~ 80% of mark
class TestCountSubstrings(unittest.TestCase):

    errorMessage = "substring {} occurs in {} {} time(s)"

    def test_no_occurence(self):
        sub = 'sub'
        strings_list = ['random', 'words', 'as', 'input']

        expected = 0
        result = count_substrings(strings_list, sub)
        msg = self.errorMessage.format(sub, strings_list, expected)
        self.assertEqual(result, expected, msg)

    def test_one_occurence(self):
        sub = 'sub'
        strings_list = ['random', 'words', 'as', 'subway', 'input', 'submarine']

        expected = 2
        result = count_substrings(strings_list, sub)
        
        msg = self.errorMessage.format(sub, strings_list, expected)
        self.assertEqual(result, expected, msg)

    def test_empty_list(self):
        sub = 'sub'
        strings_list = []

        expected = 0
        result = count_substrings(strings_list, sub)
        
        msg = self.errorMessage.format(sub, strings_list, expected)
        self.assertEqual(result, expected, msg)

    def test_empty_string_empty_list(self):
        sub = ''
        strings_list = []

        expected = 0
        result = count_substrings(strings_list, sub)
        
        msg = "empty string does not occur in " + str(strings_list)
        self.assertEqual(result, expected, msg)

    def test_empty_string_non_empty_list(self):
        sub = ''
        strings_list = ['word1', 'word2']

        expected_0 = 2 # if students implement version for returning number of strings in strings_list that have ''
        expected_1 = 12 # if students implement version of checking number of occurences that appear in strings_list

        result = count_substrings(strings_list, sub)
        
        msg = "Empty string appears in {} either {} or {} depending on implementation. Got {}"
        self.assertTrue(((result == expected_0) or (result == expected_1)), msg.format(strings_list, expected_0, expected_1, result))

class TestSeparate(unittest.TestCase):

    errorMessage = "{} is not separated to {}"
    alreadySeparatedMessage = "{} is already separated"

    def test_happy_path(self):
        mixed = '.()2xx333m01?!m13a2a0#'
        expected = '.()233301?!1320#xxmmaa'
        result = separate(mixed)

        msg = self.errorMessage.format(mixed, expected)
        self.assertEqual(result, expected, msg)

    def test_not_mixed(self):
        mixed = '21397xla&$jso@q'
        expected = '21397&$@xlajsoq'
        result = separate(mixed)

        msg = self.alreadySeparatedMessage.format(mixed)
        self.assertEqual(result, expected, msg)

    def test_empty_string(self):
        mixed = ''
        expected = ''
        result = separate(mixed)

        msg = self.alreadySeparatedMessage.format(mixed)
        self.assertEqual(result, expected, msg)

    def test_only_non_letters(self):
        mixed = '1*!3@322&49'
        expected = mixed
        result = separate(mixed)

        msg = self.alreadySeparatedMessage.format(mixed)
        self.assertEqual(result, expected, msg)

    def test_only_letters(self):
        mixed = 'abdacads'
        expected = mixed
        result = separate(mixed)

        msg = self.alreadySeparatedMessage.format(mixed)
        self.assertEqual(result, expected, msg)
    
    def test_reversed_order(self):
        mixed = 'jalmsx@*9011#(84'
        expected = '@*9011#(84jalmsx'
        result = separate(mixed)

        msg = self.errorMessage.format(mixed, expected)
        self.assertEqual(result, expected, msg)

class TestNucleobaseComplements(unittest.TestCase):
    errorMessage = "Improper nucleobase complement for {}"

    def test_happy_path(self):
        nucleobase = 'ATGCAG'
        expected = 'TACGTC'

        result = nucleobase_complements(nucleobase)

        msg = self.errorMessage.format(nucleobase)
        self.assertEqual(result, expected)

    def test_repeated(self):
        nucleobase = 'TTTTTTT'
        expected = 'AAAAAAA'

        result = nucleobase_complements(nucleobase)

        msg = self.errorMessage.format(nucleobase)
        self.assertEqual(result, expected)

class TestAreNucleobaseComplements(unittest.TestCase):
    errorMessageTrue = "{} and {} are compliments."
    errorMessageFalse = "{} and {} are not compliments."

    def test_truthy(self):
        nucleobase0 = 'GGATCCTA'
        nucleobase1 = 'CCTAGGAT'
        result = are_nucleobase_complements(nucleobase0, nucleobase1)
        msg = self.errorMessageTrue.format(nucleobase0, nucleobase1)
        self.assertTrue(result, msg)

    def test_falsy(self):
        nucleobase0 = 'GGATCATA'
        nucleobase1 = 'CCTAGGAT'
        
        result = are_nucleobase_complements(nucleobase0, nucleobase1)

        msg = self.errorMessageFalse.format(nucleobase0, nucleobase1)

        # Do not use assertFalse since None is Falsy
        self.assertEqual(result, False, msg)
    
    def test_different_lengths(self):
        nucleobase0 = 'GGATCATA'
        nucleobase1 = 'CCTAG'
        
        result = are_nucleobase_complements(nucleobase0, nucleobase1)

        msg = self.errorMessageFalse.format(nucleobase0, nucleobase1)

        # Do not use assertFalse since None is Falsy
        self.assertEqual(result, False, msg)

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)

