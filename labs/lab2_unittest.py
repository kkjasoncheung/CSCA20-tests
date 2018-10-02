import unittest
import storm
import triangle


class TestTriangleArea(unittest.TestCase):

    errorMessage = 'Incorrect area.'
    def testIntegerBaseHeight(self):
        base = 12
        height = 15

        result = triangle.triangle_area(base, height)
        expected = base * height * 0.5

        self.assertEqual(result, expected, self.errorMessage)

    def testFloatBaseIntegerHeight(self):
        base = 12.12489
        height = 15

        result = triangle.triangle_area(base, height)
        expected = base * height * 0.5

        self.assertAlmostEqual(result, expected, places = 7, msg=self.errorMessage, delta=0.0000001)

    def testIntegerBaseFloatHeight(self):
        base = 12
        height = 15.123

        result = triangle.triangle_area(base, height)
        expected = base * height * 0.5

        self.assertAlmostEqual(result, expected, places = 7, msg=self.errorMessage, delta=0.0000001)

    def testFloatBaseFloatHeight(self):
        base = 12.123
        height = 15.123

        result = triangle.triangle_area(base, height)
        expected = base * height * 0.5

        self.assertAlmostEqual(result, expected, places = 7, msg=self.errorMessage, delta=0.0000001)

    def testZeroBaseNonZeroHeight(self):
        base = 0
        height = 15.123

        result = triangle.triangle_area(base, height)
        expected = base * height * 0.5

        self.assertAlmostEqual(result, expected, places = 7, msg=self.errorMessage, delta=0.0000001)

    def testNonZeroBaseZeroHeight(self):
        base = 15.123
        height = 0

        result = triangle.triangle_area(base, height)
        expected = base * height * 0.5

        self.assertAlmostEqual(result, expected, places = 7, msg=self.errorMessage, delta=0.0000001)

class TestStormCategory(unittest.TestCase):

    errorMessage = 'Incorrect storm category.'

    def testCategoryZero(self):
        windSpeed = 100
        
        result = storm.storm_category(windSpeed)
        expected_category = 0

        self.assertEqual(result, expected_category, self.errorMessage)

    def testCategoryFive(self):
        windSpeed = 1000
        
        result = storm.storm_category(windSpeed)
        expected_category = 5

        self.assertEqual(result, expected_category, self.errorMessage)

    def testCategoryZeroBound(self):
        windSpeed = 118
        
        result = storm.storm_category(windSpeed)
        expected_category = 0

        self.assertEqual(result, expected_category, self.errorMessage)

    def testCategoryOneLowerBound(self):
        windSpeed = 119
        
        result = storm.storm_category(windSpeed)
        expected_category = 1

        self.assertEqual(result, expected_category, self.errorMessage)
    
    def testCategoryOneUpperBound(self):
        windSpeed = 153
        
        result = storm.storm_category(windSpeed)
        expected_category = 1

        self.assertEqual(result, expected_category, self.errorMessage)

    def testCategoryTwoLowerBound(self):
        windSpeed = 154
        
        result = storm.storm_category(windSpeed)
        expected_category = 2

        self.assertEqual(result, expected_category, self.errorMessage)
    
    def testCategoryTwoUpperBound(self):
        windSpeed = 177
        
        result = storm.storm_category(windSpeed)
        expected_category = 2

        self.assertEqual(result, expected_category, self.errorMessage)
    
    def testCategoryThreeLowerBound(self):
        windSpeed = 178
        
        result = storm.storm_category(windSpeed)
        expected_category = 3

        self.assertEqual(result, expected_category, self.errorMessage)
    
    def testCategoryThreeUpperBound(self):
        windSpeed = 208
        
        result = storm.storm_category(windSpeed)
        expected_category = 3

        self.assertEqual(result, expected_category, self.errorMessage)

    def testCategoryFourLowerBound(self):
        windSpeed = 209
        
        result = storm.storm_category(windSpeed)
        expected_category = 4

        self.assertEqual(result, expected_category, self.errorMessage)
    
    def testCategoryFourUpperBound(self):
        windSpeed = 251
        
        result = storm.storm_category(windSpeed)
        expected_category = 4

        self.assertEqual(result, expected_category, self.errorMessage)

    def testCategoryFiveLowerBound(self):
        windSpeed = 252
        
        result = storm.storm_category(windSpeed)
        expected_category = 5

        self.assertEqual(result, expected_category, self.errorMessage)

    def testCategoryOne(self):
        windSpeed = 120
        
        result = storm.storm_category(windSpeed)
        expected_category = 1

        self.assertEqual(result, expected_category, self.errorMessage)

    def testCategoryTwo(self):
        windSpeed = 160
        
        result = storm.storm_category(windSpeed)
        expected_category = 2

        self.assertEqual(result, expected_category, self.errorMessage)

    def testCategoryThree(self):
        windSpeed = 200
        
        result = storm.storm_category(windSpeed)
        expected_category = 3

        self.assertEqual(result, expected_category, self.errorMessage)

    def testCategoryFour(self):
        windSpeed = 220
        
        result = storm.storm_category(windSpeed)
        expected_category = 4

        self.assertEqual(result, expected_category, self.errorMessage)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)



    