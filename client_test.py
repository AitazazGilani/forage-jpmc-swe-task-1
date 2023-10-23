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
      self.assertEqual(getDataPoint(quote),(quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'],((quote['top_bid']['price']+quote['top_ask']['price'])/2)))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote),(quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'],((quote['top_bid']['price']+quote['top_ask']['price'])/2)))


  """ ------------ Add more unit tests ------------ """
  def test_getRatio(self):
    prices_a = [121.2, 0, 119.2, 121.68]
    prices_b = [121.68, 121.68, 0, 119.2]

    #price b is larger than a
    self.assertEqual(getRatio(prices_a[0], prices_b[0]), prices_a[0]/prices_b[0])

    #price_a is 0, should return 0 
    self.assertEqual(getRatio(prices_a[1], prices_b[1]), 0)

    #price_b is 0, should invoke the edge case and return none
    self.assertEqual(getRatio(prices_a[2], prices_b[2]), None)

    #price a is larger than b
    self.assertEqual(getRatio(prices_a[3], prices_b[3]), prices_a[3]/prices_b[3])



if __name__ == '__main__':
    unittest.main()
