import unittest
import asyncio
import csv
from utils import read_data, get_data
import logging

logger = logging.getLogger('websockets.client')
logger.disabled = True
loop = asyncio.get_event_loop()


class Tests(unittest.TestCase):

    def test_correct_file_headers(self):
        '''Test data.csv headers'''
        with open('csv/data.csv', 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            self.assertListEqual(header, ['Brand', 'Name'])
    
    def test_get_data(self):
        '''Test reading from wrong path'''
        result = read_data('wrong path')
        self.assertEqual(result, None)
    
    def test_read_data(self):
        '''Test reading empty name'''
        result = loop.run_until_complete(get_data('test',''))
        self.assertEqual(result, 'not found')


if __name__ == '__main__':
    unittest.main()
