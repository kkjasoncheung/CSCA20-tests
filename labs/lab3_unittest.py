import subprocess
import unittest
import lab3_p0

class TestIsLong(unittest.TestCase):
    
    def test_long_string(self):
        test_str = 'This is a very long string'
        expected = 'very long'
        result = lab3_p0.is_long(test_str)

        self.assertEqual(result, expected, "This should return 'very long' ")

    def test_short_string(self):
        test_str = 'short'
        expected = 'kinda short'
        result = lab3_p0.is_long(test_str)

        self.assertEqual(result, expected, "This should return 'kinda short' ")

    def test_string_length_10(self):
        test_str = '0123456789'
        expected = 'kinda short'
        result = lab3_p0.is_long(test_str)

        self.assertEqual(result, expected, "This should return 'kinda short' ")

class TestShorter(unittest.TestCase):

    def test_string0_shorter(self):
        string0 = 'first'
        string1 = 'second'
        expected = len(string0)
        result = lab3_p0.shorter(string0, string1)

        self.assertEqual(result, expected, "Should return " + str(expected))

    def test_string1_shorter(self):
        string0 = 'longer'
        string1 = 'short'
        expected = len(string1)
        result = lab3_p0.shorter(string0, string1)

        self.assertEqual(result, expected, "Should return " + str(expected))
    
    def test_equal_length_strings(self):
        string0 = 'same'
        string1 = 'same'
        expected = len(string0)
        result = lab3_p0.shorter(string0, string1)

        self.assertEqual(result, expected, "Should return " + str(expected))

class TestLater(unittest.TestCase):

    def test_string0_is_later(self):
        string0 = 'zoo'
        string1 = 'tiger'
        expected = string0
        result = lab3_p0.later(string0, string1)

        self.assertEqual(result, expected, "Should return " + expected)

    def test_string1_is_later(self):
        string0 = 'tiger'
        string1 = 'zoo'
        expected = string1
        result = lab3_p0.later(string0, string1)

        self.assertEqual(result, expected, "Should return " + expected)

    def test_same_strings(self):
        string0 = 'tiger'
        string1 = string0
        expected = string1
        result = lab3_p0.later(string0, string1)

        self.assertEqual(result, expected, "Should return " + expected)

    def test_same_root_string(self):
        string0 = 'tiger'
        string1 = 'tigers'
        expected = string1
        result = lab3_p0.later(string0, string1)

        self.assertEqual(result, expected, "Should return " + expected)

class TestWhere(unittest.TestCase):

    def test_letter_in_string(self):
        string0 = 'test'
        string1 = 's'
        expected = 2
        result = lab3_p0.where(string0, string1)

        self.assertEqual(result, expected, "Should return " + str(expected))

    def test_letter_in_string_double(self):
        string0 = 'test'
        string1 = 't'
        expected = 0
        result = lab3_p0.where(string0, string1)

        self.assertEqual(result, expected, "Should return " + str(expected))

    def test_letter_not_in_string(self):
        string0 = 'test'
        string1 = 'a'
        expected = -1
        result = lab3_p0.where(string0, string1)

        self.assertEqual(result, expected, "Should return " + str(expected))

class TestIsVowel(unittest.TestCase):

    def test_is_vowel_true(self):
        test_string = 'a'
        expected = True
        result = lab3_p0.is_vowel(test_string)

        self.assertEqual(result, expected, "Should return " + str(expected))

    def test_is_not_vowel_true(self):
        test_string = 'z'
        expected = False
        result = lab3_p0.is_vowel(test_string)

        self.assertEqual(result, expected, "Should return " + str(expected))

class TestFunctionCalls(unittest.TestCase):
    
    def test_printHelloWorld(self):
        # Grab standard output from importing module
        proc = subprocess.Popen(["python", "-c", "import lab3_p1;"], stdout=subprocess.PIPE)
        # Deocde output to string
        out = proc.communicate()[0].decode()
        # print out the output
        print("output from lab3_p1")
        result = out.split()
        print(result)
        expected = ['kinda', 'short', 'very', 'long', '1', '3', 'bcd', 'cde', '0', '-1', 'True', 'False']

        sameLength = len(result) == len(expected)
        
        if (not(sameLength)):
            self.assertTrue(False, 'The length of your output does not match')
        
        correctMatches = 0
        
        for i in range(len(expected)):
            if (result[i] == expected[i]):
                correctMatches += 1

        self.assertEqual(correctMatches, len(expected), "Incorrect outputs")

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)