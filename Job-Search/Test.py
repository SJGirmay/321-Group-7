import unittest
from unittest.mock import patch
import main.py

class Test(unittest.TestCase):

    @patch('builtins.input', side_effect=['yes', 'Virginia', 'Nurse'])
    def test_using_side_effect(self, mock_input):
        calling_1 = mock_input()
        calling_2 = mock_input()
        calling_3 = mock_input()
        self.assertTrue(calling_1 == 'yes' and calling_2 == 'Virginia' and
                        calling_3 == 'Nurse')
class Test1(unittest.TestCase):

    @patch('builtins.input', side_effect=['no', 'Mars', 'Nurse'])
    def test_using_side_effect(self, mock_input):
        calling_1 = mock_input()
        calling_2 = mock_input()
        calling_3 = mock_input()
        self.assertTrue(calling_1 == 'yes' and calling_2 == 'Virginia' and
                        calling_3 == 'cop')
class Test2(unittest.TestCase):

    @patch('builtins.input', side_effect=['no', 'Mars', 'Nurse'])
    def test_using_side_effect(self, mock_input):
        calling_1 = mock_input()
        calling_2 = mock_input()
        calling_3 = mock_input()
        self.assertTrue(calling_1 == 'yes' and calling_2 == 'Virginia' and
                        calling_3 == 'Doctor')
class Test3(unittest.TestCase):

    @patch('builtins.input', side_effect=['no', 'Mars', 'Nurse'])
    def test_using_side_effect(self, mock_input):
        calling_1 = mock_input()
        calling_2 = mock_input()
        calling_3 = mock_input()
        self.assertTrue(calling_1 == 'yes' and calling_2 == 'Kaprickom' and
                        calling_3 == '')
class Test4(unittest.TestCase):

    @patch('builtins.input', side_effect=['no', 'Mars', 'Nurse'])
    def test_using_side_effect(self, mock_input):
        calling_1 = mock_input()
        calling_2 = mock_input()
        calling_3 = mock_input()
        self.assertTrue(calling_1 == 'yes' and calling_2 == 'Massachussets' and
                        calling_3 == 'Nurse')
class Test5(unittest.TestCase):

    @patch('builtins.input', side_effect=['no', 'Mars', 'Nurse'])
    def test_using_side_effect(self, mock_input):
        calling_1 = mock_input()
        calling_2 = mock_input()
        calling_3 = mock_input()
        self.assertTrue(calling_1 == 'yes' and calling_2 == 'Pog' and
                        calling_3 == 'Nurse')
if __name__ == "__main__":
  unittest.main()
