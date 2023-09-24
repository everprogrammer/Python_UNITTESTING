import unittest

import mock
from io import StringIO
from OOP_File.files import Files



class TestIntegrationFiles(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.fObj = Files()

    def test_isObjCorrectType(self):
        self.assertIsInstance(self.fObj, Files)

    def test_readFileValid(self):
        self.fObj.set_filename('test_data.txt')
        data = self.fObj.read_file()    # "Hello"
        self.assertEqual(data, ['Hello'])

    def test_readFileInvalid(self):
        self.fObj.set_filename('no_test_data.txt')
        with self.assertRaises(FileNotFoundError):
            data = self.fObj.read_file()    

    def test_checkRealData(self):
        self.fObj.set_filename('data.txt')
        data = self.fObj.read_file()
        headers = data[0].split(' ')
        headers[-1] = headers[-1].replace('!\n', '')
        # breakpoint()
        expected_output = ['Line', '1', 'of', 'test', 'file']
        for i in range(len(headers)):
            self.assertEqual(headers[i], expected_output[i])




