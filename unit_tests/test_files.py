import unittest
import mock
from OOP_File.files import Files


"""
What should be tested?
- can create an object
- test read_file()
- test write_file()
"""

"""
Notes: 
unittests -> isolated; decoupled from any external dependencies
"""

class TestFiles(unittest.TestCase):
    def test_canCreateObj(self):
        Obj1 = Files()
        Obj2 = Files('not-exist.txt')
        self.assertIsNone(Obj1.filename)
        self.assertIsNotNone(Obj2.filename)
    
    def test_readFile(self):
        """
        Below Not unit test: more like an INTEGRATION TEST!
        --> with mock.patch() [temp scope]
        1) to inject 
        """
        # fObj = Files('data.txt')
        # data = fObj.read_file()
        # expected = ['Line 1 of test file!\n', 'Line 2 of test file!\n', 'Line 3 of test file!']
        # self.assertEqual(data, expected)

        # open = mock.mock_open(read_data='EXPECTED')
        # mockedFile = open('fake.txt', 'r')
        # data = mockedFile.read()
        # self.assertEqual(data, "EXPECTED")

        fObj = Files('fake.txt')
        with mock.patch('builtins.open', mock.mock_open(read_data='EXPECTED')):
            data = fObj.read_file()
            self.assertEqual(data, ['EXPECTED'])
    

