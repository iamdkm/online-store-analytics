import unittest
import pandas as pd
from analytics import OnlineStoreAnalytics


class TestOnlineStoreAnalytics(unittest.TestCase):
    def setUp(self):
        '''
        we can have different test_orders.csv files(and take that from arguments) to test on multiple files 
        and and based on the test file we can have below assertion tests to get expected output from 
        the respective output files for the test_orders.csv
        Here, I have kept the testing simple.
        '''
        self.analytics = OnlineStoreAnalytics('test_orders.csv')

    def test_monthly_revenue(self):
        # Assuming the known dataset for testing
        result = self.analytics.calculate_monthly_revenue()

        # Example assertions based on the known dataset
        # Sum of revenue for January
        self.assertEqual(result['2023-01'].sum(), 82.0)
        # self.assertEqual(result['2023-02'].sum(), 55.0)  # Sum of revenue for February
        # Sum of revenue for March
        self.assertEqual(result['2023-03'].sum(), 12.0)
        # Sum of revenue for April
        self.assertEqual(result['2023-04'].sum(), 40.0)
        # Sum of revenue for May
        self.assertEqual(result['2023-05'].sum(), 54.0)
        # Sum of revenue for June
        self.assertEqual(result['2023-06'].sum(), 35.0)
        # Sum of revenue for July
        self.assertEqual(result['2023-07'].sum(), 63.0)
        # Sum of revenue for August
        self.assertEqual(result['2023-08'].sum(), 38.0)
        # Sum of revenue for September
        self.assertEqual(result['2023-09'].sum(), 22.0)
        # Sum of revenue for October
        self.assertEqual(result['2023-10'].sum(), 57.0)
        # Sum of revenue for November
        self.assertEqual(result['2023-11'].sum(), 35.0)
        # Sum of revenue for December
        self.assertEqual(result['2023-12'].sum(), 10.0)

    def test_product_revenue(self):
        result = self.analytics.calculate_product_revenue()

        # self.assertEqual(result['ProductA'], 20.0)  # Total revenue for ProductA
        # Total revenue for ProductB
        self.assertEqual(result['ProductB'], 35.0)
        # self.assertEqual(result['ProductC'], 15.0)  # Total revenue for ProductC
        # Total revenue for ProductD
        self.assertEqual(result['ProductD'], 79.0)
        # Total revenue for ProductE
        self.assertEqual(result['ProductE'], 63.0)
        # Total revenue for ProductF
        self.assertEqual(result['ProductF'], 68.0)
        # Total revenue for ProductG
        self.assertEqual(result['ProductG'], 108.0)
        # Total revenue for ProductH
        self.assertEqual(result['ProductH'], 45.0)
        # Total revenue for ProductI
        self.assertEqual(result['ProductI'], 28.0)
        # Total revenue for ProductJ
        self.assertEqual(result['ProductJ'], 22.0)

    def test_customer_revenue(self):
        result = self.analytics.calculate_customer_revenue()

        self.assertEqual(result[101], 12.0)  # Total revenue for Customer 101
        self.assertEqual(result[102], 22.0)  # Total revenue for Customer 102
        self.assertEqual(result[103], 35.0)  # Total revenue for Customer 103
        self.assertEqual(result[104], 60.0)  # Total revenue for Customer 104
        self.assertEqual(result[105], 88.0)  # Total revenue for Customer 105
        # self.assertEqual(result[106], 22.0)  # Total revenue for Customer 106
        self.assertEqual(result[107], 22.0)  # Total revenue for Customer 107
        self.assertEqual(result[108], 95.0)  # Total revenue for Customer 108
        self.assertEqual(result[109], 50.0)  # Total revenue for Customer 109
        self.assertEqual(result[110], 64.0)  # Total revenue for Customer 110

    def test_top_customers(self):
        result = self.analytics.get_top_customers()

        # Top customers in descending order
        self.assertEqual(result.index.tolist(), [
                         108, 105, 110, 104, 109, 103, 102, 107, 101])
        # Revenue for the top customer (Customer 108)
        self.assertEqual(result[108], 95.0)
        self.assertEqual(result[105], 88.0)
        self.assertEqual(result[110], 64.0)
        self.assertEqual(result[104], 60.0)
        self.assertEqual(result[109], 50.0)


if __name__ == '__main__':
    unittest.main()
