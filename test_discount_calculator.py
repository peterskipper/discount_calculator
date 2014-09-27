import unittest
from discount_calculator import calculate_discount

class DiscountCalculatorTests(unittest.TestCase):
    def testPriceRange(self):
        #insert code here to check that initial price is > zero
        with self.assertRaises(ValueError):
            calculate_discount(0,10,20)
    def testDiscountRange(self):
        #insert code here to check that discounts are >= zero and below 100 together
        with self.assertRaises(ValueError):
            calculate_discount(100,-5,-10)
        with self.assertRaises(ValueError):
            calculate_discount(100,50,60)
    def testZeroDiscount(self):
        #insert code to check here that at least one discount is nonzero
        with self.assertRaises(ValueError):
            calculate_discount(100,0,0)
    def testHappyPath(self):
        #insert code here to check that func works under normal circumstances
        discounted_cost = calculate_discount(100,10,30)
        self.assertEqual(discounted_cost, 60.0)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DiscountCalculatorTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
    