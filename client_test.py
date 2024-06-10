import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            data_point = getDataPoint(quote)
            price = data_point[-1]
            self.assertEqual(price, (quote['top_bid']['price'] + quote['top_ask']['price']) / 2)


    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            data_point = getDataPoint(quote)
            price = data_point[-1]
            self.assertEqual(price, (quote['top_bid']['price'] + quote['top_ask']['price']) / 2)

    """ ------------ Add more unit tests ------------ """
    def test_getRatio_returnsRatio(self):
        prices = [(121.2, 120.48), (121.68, 117.87), (121.2, 0)]
        for price in prices:
            expected_ratio = None if price[1] == 0 else price[0] / price[1]
            self.assertEqual(expected_ratio, getRatio(*price))


if __name__ == '__main__':
    unittest.main()
