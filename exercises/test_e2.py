import unittest
from e2 import *

# allow students to be off by 5 cents

errorMsg = "Tax rate is not correct"

class TestMarginalTaxRate(unittest.TestCase):

    def test_happyPath(self):
        income = 110000
        result = marginal_tax_rate(income)
        expected = 0.26

        self.assertEqual(result, expected, errorMsg)

    def test_zeroIncome(self):
        income = 0
        result = marginal_tax_rate(income)
        expected = 0.15

        self.assertEqual(result, expected, errorMsg)        

    def test_firstBracketUpperBound(self):
        income = 46605
        result = marginal_tax_rate(income)
        expected = 0.15

        self.assertEqual(result, expected, errorMsg)

    def test_secondBracketLowerBound(self):
        income = 46605.01
        result = marginal_tax_rate(income)
        expected = 0.205

        self.assertEqual(result, expected, errorMsg)

    def test_secondBracketUpperBound(self):
        income = 93208
        result = marginal_tax_rate(income)
        expected = 0.205

        self.assertEqual(result, expected, errorMsg)

    def test_thirdBracketLowerBound(self):
        income = 93208.01
        result = marginal_tax_rate(income)
        expected = 0.26

        self.assertEqual(result, expected, errorMsg)

    def test_thirdBracketUpperBound(self):
        income = 144489
        result = marginal_tax_rate(income)
        expected = 0.26

        self.assertEqual(result, expected, errorMsg)

    def test_forthBracketLowerBound(self):
        income = 144489.01
        result = marginal_tax_rate(income)
        expected = 0.29

        self.assertEqual(result, expected, errorMsg)

    def test_forthBracketUpperBound(self):
        income = 205842
        result = marginal_tax_rate(income)
        expected = 0.29

        self.assertEqual(result, expected, errorMsg)

    def test_fifthBracketLowerBound(self):
        income = 205842.01
        result = marginal_tax_rate(income)
        expected = 0.33

        self.assertEqual(result, expected, errorMsg)

    def test_superRich(self):
        income = 1000000
        result = marginal_tax_rate(income)
        expected = 0.33

        self.assertEqual(result, expected, errorMsg)

class TestAverageTaxRate(unittest.TestCase):

    EPSILON = 1e-6
    def test_happyPath(self):
        income = 100000
        result = average_tax_rate(income)
        expected = 0.18310285

        self.assertAlmostEqual(result, expected, msg=errorMsg, delta=self.EPSILON)

    def test_zeroIncome(self):
        income = 0
        result = average_tax_rate(income)
        expected = 0.15

        self.assertAlmostEqual(result, expected, msg=errorMsg, delta=self.EPSILON) 

    def test_firstBracket(self):
        income = 35273
        result = average_tax_rate(income)
        expected = 0.15

        self.assertAlmostEqual(result, expected, msg=errorMsg, delta=self.EPSILON) 

    def test_secondBracket(self):
        income = 50000
        result = average_tax_rate(income)
        expected = 0.1537345

        self.assertAlmostEqual(result, expected, msg=errorMsg, delta=self.EPSILON) 
    
    def test_thirdBracket(self):
        income = 123456
        result = average_tax_rate(income)
        expected = 0.19771291

        self.assertAlmostEqual(result, expected, msg=errorMsg, delta=self.EPSILON) 

    def test_forthBracket(self):
        income = 175808
        result = average_tax_rate(income)
        expected = 0.221605018

        self.assertAlmostEqual(result, expected, msg=errorMsg, delta=self.EPSILON) 
    
    def test_fifthBracket(self):
        income = 350234
        result = average_tax_rate(income)
        expected = 0.272158485

        self.assertAlmostEqual(result, expected, msg=errorMsg, delta=self.EPSILON) 

class TestTotalIncomeTax(unittest.TestCase):
    
    incomeError = "Incorrect total income tax"

    def test_happyPath(self):
        income = 100000
        result = total_income_tax(income)
        expected = 18310.28

        self.assertAlmostEqual(result, expected, msg=self.incomeError, delta=0.05)

    def test_zeroIncome(self):
        income = 0
        result = total_income_tax(income)
        expected = 0

        self.assertAlmostEqual(result, expected, msg=self.incomeError, delta=0.05)

    def test_firstBracket(self):
        income = 35273
        result = total_income_tax(income)
        expected = 5290.95

        self.assertAlmostEqual(result, expected, msg=self.incomeError, delta=0.05)

    def test_secondBracket(self):
        income = 50000
        result = total_income_tax(income)
        expected = 7686.73

        self.assertAlmostEqual(result, expected, msg=self.incomeError, delta=0.05)

    def test_thirdBracket(self):
        income = 123456
        result = total_income_tax(income)
        expected = 24408.85

        self.assertAlmostEqual(result, expected, msg=self.incomeError, delta=0.05)

    def test_forthBracket(self):
        income = 175808
        result = total_income_tax(income)
        expected = 38959.94

        self.assertAlmostEqual(result, expected, msg=self.incomeError, delta=0.05)

    def test_fifthBracket(self):
        income = 350234
        result = total_income_tax(income)
        expected = 95319.16

        self.assertAlmostEqual(result, expected, msg=self.incomeError, delta=0.05)

    def test_forthBracketLowerBound(self):
        income = 144489.01
        result = total_income_tax(income)
        expected = 29877.43

        self.assertAlmostEqual(result, expected, msg=self.incomeError, delta=0.05)

    def test_forthBracketUpperBound(self):
        income = 205842
        result = total_income_tax(income)
        expected = 47669.80

        self.assertAlmostEqual(result, expected, msg=self.incomeError, delta=0.05)

    def test_thirdBracketUpperBound(self):
        income = 144489
        result = total_income_tax(income)
        expected = 29877.43

        self.assertAlmostEqual(result, expected, msg=self.incomeError, delta=0.05)

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
