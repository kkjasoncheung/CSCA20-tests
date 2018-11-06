import unittest
import csv
import pep8
import e5
import e5_soln

CHECK_FILE = ['e5.py']

# PEP8 tests: 20% of mark
class TestPEP8(unittest.TestCase):

    def test_pep8_0(self):
        pep8style = pep8.StyleGuide(quiet=True,
                                    max_line_length=120,
                                    ignore=('E121', 'E123', 'E126', 'E133',
                                            'E211', 'E226', 'E241', 'E242', 'E704', 'W503'))
        result = pep8style.check_files(CHECK_FILE)

        report_output = "Found code style errors (and warnings):"
        for code in result.messages:
            message = result.messages[code]
            count = result.counters[code]
            report_output += "\n" + code + ": " + message + " (" + str(count) + ")"

        self.assertEqual(result.total_errors, 0, report_output)
    
    def test_pep8_1(self):
        pep8style = pep8.StyleGuide(quiet=True,
                                    max_line_length=120,
                                    ignore=('E121', 'E123', 'E126', 'E133',
                                            'E211', 'E226', 'E241', 'E242', 'E704', 'W503'))
        result = pep8style.check_files(CHECK_FILE)

        report_output = "Found code style errors (and warnings):"
        for code in result.messages:
            message = result.messages[code]
            count = result.counters[code]
            report_output += "\n" + code + ": " + message + " (" + str(count) + ")"

        self.assertEqual(result.total_errors, 0, report_output)

    def test_pep8_2(self):
        pep8style = pep8.StyleGuide(quiet=True,
                                    max_line_length=120,
                                    ignore=('E121', 'E123', 'E126', 'E133',
                                            'E211', 'E226', 'E241', 'E242', 'E704', 'W503'))
        result = pep8style.check_files(CHECK_FILE)

        report_output = "Found code style errors (and warnings):"
        for code in result.messages:
            message = result.messages[code]
            count = result.counters[code]
            report_output += "\n" + code + ": " + message + " (" + str(count) + ")"

        self.assertEqual(result.total_errors, 0, report_output)

    def test_pep8_3(self):
        pep8style = pep8.StyleGuide(quiet=True,
                                    max_line_length=120,
                                    ignore=('E121', 'E123', 'E126', 'E133',
                                            'E211', 'E226', 'E241', 'E242', 'E704', 'W503'))
        result = pep8style.check_files(CHECK_FILE)

        report_output = "Found code style errors (and warnings):"
        for code in result.messages:
            message = result.messages[code]
            count = result.counters[code]
            report_output += "\n" + code + ": " + message + " (" + str(count) + ")"

        self.assertEqual(result.total_errors, 0, report_output)

# Correctness: 80% of mark
filename = "grades.csv"
filename_single = "grades_single.csv"
filename_single_student_mult_assignment = "grades_single_student_multiple_a.csv"
filename_mult_student_single_assignment = "grades_multiple_students_single_a.csv"

class TestSkipHeader(unittest.TestCase):
    
    errorMessage = "Expected {}, but got {}"

    def test_single_entry(self):
        f = open(filename_single, 'r')
        e5_soln.skip_header(f)
        expected = f.readline()
        f.close()

        f = open(filename_single, 'r')
        e5.skip_header(f)
        result = f.readline()
        f.close()

        self.assertEqual(result, expected, self.errorMessage.format(expected, result))

    def test_multiple_entries(self):
        f = open(filename, 'r')
        e5_soln.skip_header(f)
        expected = f.readline()
        f.close()

        f = open(filename, 'r')
        e5.skip_header(f)
        result = f.readline()
        f.close()

        self.assertEqual(result, expected, self.errorMessage.format(expected, result))

class TestGetNumAssignments(unittest.TestCase):
    
    errorMessage = "Expected {} assignment(s) but got {}"

    def test_single_assignment(self):
        expected = 1

        f = open(filename_single, 'r')
        result = e5.get_num_assignments(f)
        f.close()
    
        self.assertEqual(result, expected, self.errorMessage.format(expected, result))
    
    def test_multiple_assignments(self):
        expected = 9

        f = open(filename, 'r')
        result = e5.get_num_assignments(f)
        f.close()
    
        self.assertEqual(result, expected, self.errorMessage.format(expected, result))

class TestGetClassList(unittest.TestCase):
    
    errorMessage = "Expected class list {} but got {}"

    def test_single_student(self):
        expected = ["Squarepants, Spongebob"]

        f = open(filename_single, 'r')
        result = e5.get_class_list(f)
        f.close()
        
        self.assertEqual(result, expected, self.errorMessage.format(expected, result))
    
    def test_multiple_students(self):
        expected = ['Dylan, Bob', 'Wylde, Zack', 'Osbourne, Ozzy', 'Beiber, Justin', 'Gomez, Selena', 'Goulding, Ellie', 'Osbourne, Ozzy']

        f = open(filename, 'r')
        result = e5.get_class_list(f)
        f.close()
        
        self.assertEqual(result, expected, self.errorMessage.format(expected, result))

class TestStudentAvg(unittest.TestCase):
    
    errorMessage = "Expected list of tuples {} but got {}"

    def test_single_student_single_assignment(self):
        expected = [('9911991199', 99)]

        f = open(filename_single, 'r')
        result = e5.student_avg(f)
        f.close()

        self.assertEqual(result, expected, self.errorMessage.format(expected, result))
        
    def test_single_student_multiple_assignments(self):        
        expected = [('9911991199', (99 + 90 + 23 + 49 + 100 + 99 + 65)/7)]

        f = open(filename_single_student_mult_assignment, 'r')
        result = e5.student_avg(f)
        f.close()

        self.assertEqual(result, expected, self.errorMessage.format(expected, result))

    def test_multiple_students_single_assignment(self):
        expected = [('1029303928', 99.0), ('8392810201', 11.0), ('3827102839', 89.0), \
        ('9928394921', 90.0), ('1929934273', 98.0), ('2282938109', 98.0), ('3827102839', 90.0)]

        f = open(filename_mult_student_single_assignment, 'r')
        result = e5.student_avg(f)
        f.close()

        self.assertEqual(result, expected, self.errorMessage.format(expected, result))

    def test_multiple_students_multiple_assignments(self):
        expected = [('1029303928', 69.88888888888889), ('8392810201', 34.44444444444444), \
        ('3827102839', 56.333333333333336), ('9928394921', 53.111111111111114), \
        ('1929934273', 57.666666666666664), ('2282938109', 96.66666666666667), \
        ('3827102839', 17.444444444444443)]

        f = open(filename, 'r')
        result = e5.student_avg(f)
        f.close()

        self.assertEqual(result, expected, self.errorMessage.format(expected, result))

class TestWriteAvg(unittest.TestCase):
    
    out_file = "output.csv"
    
    def test_empty_list(self):
        ell = []
        e5.write_avg(ell, self.out_file)
        expected_lines = 0
        result_lines = 0

        with open(self.out_file) as csv_file:
            result_lines = len(csv_file.readlines())
            
        self.assertEqual(result_lines, expected_lines, "Your file wrote a line to out_file for ell = []")
            
    def test_non_empty_list(self):
        ell = [('1029303928', 90), ('8392810201', 11), ('3827102839', 89)]
        e5.write_avg(ell, self.out_file)
        out_file_content = []
        expected0 = ['1029303928, 90', '8392810201, 11', '3827102839, 89']
        expected1 = ['1029303928,  90', '8392810201,  11', '3827102839,  89']
        
        with open(self.out_file) as csv_file:
            out_reader = csv.reader(csv_file)
            for line in out_reader:
                out_file_content.append(line[0] + ", " + line[1])
        
        msg = "Given ell {}, contents you wrote: {} != expected contents, {}".format(ell, out_file_content, expected0)
        result = (out_file_content == expected0) or (out_file_content == expected1)
        self.assertTrue(result, msg)

class TestClassMedians(unittest.TestCase):

    errorMessage = "Expected {}, but got {} for medians"

    def test_single_student_single_assignment(self):
        expected = [99.0]

        f = open(filename_single, 'r')
        result = e5.class_medians(f)
        f.close()

        self.assertEqual(result, expected, self.errorMessage.format(expected, result))

    def test_single_student_multiple_assignments(self):
        expected = [99.0, 90.0, 23.0, 49.0, 100.0, 99.0, 65.0]

        f = open(filename_single_student_mult_assignment, 'r')
        result = e5.class_medians(f)
        f.close()

        self.assertEqual(result, expected, self.errorMessage.format(expected, result))

    def test_multiple_students_single_assignment(self):
        expected = [90.0]

        f = open(filename_mult_student_single_assignment, 'r')
        result = e5.class_medians(f)
        f.close()

        self.assertEqual(result, expected, self.errorMessage.format(expected, result))

    def test_multiple_students_multiple_assignments(self):
        expected = [90.0, 49.0, 34.0, 47.0, 44.0, 48.0, 34.0, 50.0, 60.0]

        f = open(filename, 'r')
        result = e5.class_medians(f)
        f.close()

        self.assertEqual(result, expected, self.errorMessage.format(expected, result))

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)