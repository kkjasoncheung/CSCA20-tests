import unittest
from e4 import *

EPSILON = 1e-5

# Unit Tests: ~ 80% of mark
class TestSinAll(unittest.TestCase):

    errorMessage = "Incorrect sin of the angles {}. Expected {}"

    def test_integers_only(self):
        angles_list = [0, 90, 180, 720, 1080]
        expected_angles = [0.0, 1.0, 1.2246467991473532e-16, -4.898587196589413e-16, -7.347880794884119e-16]
        result = True

        result_angles = sin_all(angles_list)
        
        for i in range(len(result_angles)):
            if not(is_close(result_angles[i], expected_angles[i], EPSILON)):
                result = False
                break

        self.assertTrue(result, self.errorMessage.format(angles_list, expected_angles))

    def test_int_and_floats(self):
        angles_list = [0, 90, 180, 360, 35.7, 22.13]
        expected_angles = [0.0, 1.0, 1.2246467991473532e-16, -2.4492935982947064e-16, 0.5835412113561176, 0.3767093408018723]
        result = True

        result_angles = sin_all(angles_list)
        
        for i in range(len(result_angles)):
            if not(is_close(result_angles[i], expected_angles[i], EPSILON)):
                result = False
                break

        self.assertTrue(result, self.errorMessage.format(angles_list, expected_angles))
    
    def test_floats_only(self):
        angles_list = [1.2, 56.2, 24.44, 1080.32]
        expected_angles = [0.020942419883356957, 0.8309844692743282, 0.4137401062348638, 0.0055850245708272276]
        result = True

        result_angles = sin_all(angles_list)
        
        for i in range(len(result_angles)):
            if not(is_close(result_angles[i], expected_angles[i], EPSILON)):
                result = False
                break

        self.assertTrue(result, self.errorMessage.format(angles_list, expected_angles))

    def test_negative_angles(self):
        angles_list = [0, -90, -180, -360, -35.7, -22.13]
        expected_angles = [0.0, -1.0, -1.2246467991473532e-16, 2.4492935982947064e-16, -0.5835412113561176, -0.3767093408018723]
        result = True

        result_angles = sin_all(angles_list)
        
        for i in range(len(result_angles)):
            if not(is_close(result_angles[i], expected_angles[i], EPSILON)):
                result = False
                break

        self.assertTrue(result, self.errorMessage.format(angles_list, expected_angles))

    def test_empty_list(self):
        angles_list = []
        
        result_angles = sin_all(angles_list)
        
        self.assertTrue(len(result_angles) == 0, self.errorMessage.format(angles_list, angles_list))


class TestSinAllInPlace(unittest.TestCase):
    
    errorMessage = "Incorrect in place sin of the angles {}. Expected {}"

    def test_integers_only(self):
        angles_list = [0, 90, 180, 720, 1080]
        expected_angles = [0.0, 1.0, 1.2246467991473532e-16, -4.898587196589413e-16, -7.347880794884119e-16]
        result = True

        sin_all_in_place(angles_list)
        
        for i in range(len(angles_list)):
            if not(is_close(angles_list[i], expected_angles[i], EPSILON)):
                result = False
                break

        self.assertTrue(result, self.errorMessage.format(angles_list, expected_angles))

    def test_int_and_floats(self):
        angles_list = [0, 90, 180, 360, 35.7, 22.13]
        expected_angles = [0.0, 1.0, 1.2246467991473532e-16, -2.4492935982947064e-16, 0.5835412113561176, 0.3767093408018723]
        result = True

        sin_all_in_place(angles_list)
        
        for i in range(len(angles_list)):
            if not(is_close(angles_list[i], expected_angles[i], EPSILON)):
                result = False
                break

        self.assertTrue(result, self.errorMessage.format(angles_list, expected_angles))
    
    def test_floats_only(self):
        angles_list = [1.2, 56.2, 24.44, 1080.32]
        expected_angles = [0.020942419883356957, 0.8309844692743282, 0.4137401062348638, 0.0055850245708272276]
        result = True

        sin_all_in_place(angles_list)
        
        for i in range(len(angles_list)):
            if not(is_close(angles_list[i], expected_angles[i], EPSILON)):
                result = False
                break

        self.assertTrue(result, self.errorMessage.format(angles_list, expected_angles))

    def test_negative_angles(self):
        angles_list = [0, -90, -180, -360, -35.7, -22.13]
        expected_angles = [0.0, -1.0, -1.2246467991473532e-16, 2.4492935982947064e-16, -0.5835412113561176, -0.3767093408018723]
        result = True

        sin_all_in_place(angles_list)
        
        for i in range(len(angles_list)):
            if not(is_close(angles_list[i], expected_angles[i], EPSILON)):
                result = False
                break

        self.assertTrue(result, self.errorMessage.format(angles_list, expected_angles))

    def test_empty_list(self):
        angles_list = []
        
        sin_all_in_place(angles_list)
        
        self.assertTrue(angles_list == [], self.errorMessage.format(angles_list, angles_list))

class TestMaxMin(unittest.TestCase):
    
    errorMessage = "Given {} the maximum of minimums should be {}"

    def test_single_sublist(self):
        ells = [[10, 20, 3, 2, 142]]
        expected = 2

        result = max_min(ells)

        self.assertEqual(result, expected, self.errorMessage.format(ells, expected))

    def test_multiple_sublists(self):
        ells = [[10, 20, 3, 2, 142], [10, 23, 3, 34], [7, 10, 2]]
        expected = 3

        result = max_min(ells)

        self.assertEqual(result, expected, self.errorMessage.format(ells, expected))

    def test_int_and_float(self):
        ells = [[10, 20.123, 3.7, 2.2, 142.12], [10.9, 239.12, 3.1, 34], [7, 10, 2.67]]
        expected = 3.1

        result = max_min(ells)

        self.assertEqual(result, expected, self.errorMessage.format(ells, expected))

    def test_duplicate_result(self):
        ells = [[10, 20.123, 3.7, 2.2, 142.12], [10.9, 239.12, 3.1, 34], [7, 3.1, 2.67]]
        expected = 3.1

        result = max_min(ells)

        self.assertEqual(result, expected, self.errorMessage.format(ells, expected))


class TestAllTitleCase(unittest.TestCase):
    
    errorMessage = "Given list {}, expected {}"

    def test_empty_list(self):
        strings = []
        expected = True

        result = all_title_case(strings)

        self.assertEqual(result, expected, self.errorMessage.format(strings, expected))

    def test_single_letters_empty_string_false(self):
        strings = ['T', 'S', 'N', '']
        expected = False

        result = all_title_case(strings)

        self.assertEqual(result, expected, self.errorMessage.format(strings, expected))

    def test_single_letter_single_entry_true(self):
        strings = ['T']
        expected = True

        result = all_title_case(strings)

        self.assertEqual(result, expected, self.errorMessage.format(strings, expected))
    
    def test_single_letter_single_entry_false(self):
        strings = ['t']
        expected = False

        result = all_title_case(strings)

        self.assertEqual(result, expected, self.errorMessage.format(strings, expected))
    
    def test_mixed_false(self):
        strings = ['T', 's', 'Nasty']
        expected = False

        result = all_title_case(strings)

        self.assertEqual(result, expected, self.errorMessage.format(strings, expected))
    
    def test_mixed_true(self):
        strings = ['Toilet', 'Smells', 'Nasty']
        expected = True

        result = all_title_case(strings)

        self.assertEqual(result, expected, self.errorMessage.format(strings, expected))


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
