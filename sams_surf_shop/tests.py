# Write your code below:

import unittest
import surfshop
import datetime

class SrufShopTests(unittest.TestCase):
    # setup shoppingCart method
    def setUp(self):
        self.cart = surfshop.ShoppingCart()

    # test add_surfboards method
    def test_add_one_surfboard(self):
        self.assertEqual(self.cart.add_surfboards(), 'Successfully added 1 surfboard to cart!')
        self.assertEqual(self.cart.num_surfboards, 1)


    # test add_surfboards method with three input values (2, 3, 4) using subTest
    def test_add_more_surfboards(self):
        for num in range(2,5):
            with self.subTest(num=num):
                message = self.cart.add_surfboards(num)
                self.assertEqual(message, f'Successfully added {num} surfboards to cart!')
                self.assertEqual(self.cart.num_surfboards, num)
                self.cart = surfshop.ShoppingCart()

    # test TooManyBoardsError
    # skip this test
    # @unittest.skip('In Off Season; Skipping test')
    def test_too_many_boards_error(self):
        self.cart.add_surfboards(4)
        with self.assertRaises(surfshop.TooManyBoardsError):
            self.cart.add_surfboards()

    # test local discount method
    # @unittest.expectedFailure
    def test_locals_discount(self):
        self.cart.apply_locals_discount()
        self.assertTrue(self.cart.locals_discount)


    def test_checkout_invalid_date(self):
        right_now = datetime.datetime.now() + datetime.timedelta(days=1)
        self.assertRaises(surfshop.CheckoutDateError, self.cart.set_checkout_date, right_now)


unittest.main()




