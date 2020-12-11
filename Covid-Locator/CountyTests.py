import unittest
from unittest.mock import patch

import CountyMenu

class TestCounty(unittest.TestCase):

    @patch('builtins.input', side_effect=['Alabama', 'Washington'])
    def test_County1(self, mock_inputs):
        self.assertEqual(CountyMenu.CountyMenu(), "Success")

    @patch('builtins.input', side_effect=['VA', 'Fairfax'])
    def test_County2(self, mock_inputs):
        self.assertEqual(CountyMenu.CountyMenu(), "Success")

    @patch('builtins.input', side_effect=['virginia', 'Fairfax'])
    def test_County3(self, mock_inputs):
        self.assertEqual(CountyMenu.CountyMenu(), "Success")

    @patch('builtins.input', side_effect=['Virginia', 'Fairfax'])
    def test_County4(self, mock_inputs):
        self.assertEqual(CountyMenu.CountyMenu(), "Success")

    @patch('builtins.input', side_effect=['alabama', 'Washington'])
    def test_County5(self, mock_inputs):
        self.assertEqual(CountyMenu.CountyMenu(), "Success")

    @patch('builtins.input', side_effect=['Alabama', 'Washing'])
    def test_County6(self, mock_inputs):
        self.assertEqual(CountyMenu.CountyMenu(), None)

    @patch('builtins.input', side_effect=['Virginia', 'Waaa'])
    def test_County7(self, mock_inputs):
        self.assertEqual(CountyMenu.CountyMenu(), None)

    @patch('builtins.input', side_effect=['FL', 'Washington'])
    def test_County8(self, mock_inputs):
        self.assertEqual(CountyMenu.CountyMenu(), "Success")
    
    @patch('builtins.input', side_effect=['maryland', 'Howard'])
    def test_County9(self, mock_inputs):
        self.assertEqual(CountyMenu.CountyMenu(), "Success")

    @patch('builtins.input', side_effect=['Virginia', 'fair'])
    def test_County10(self, mock_inputs):
        self.assertEqual(CountyMenu.CountyMenu(), None)

    @patch('builtins.input', side_effect=['New York', 'Clintonn'])
    def test_County11(self, mock_inputs):
        self.assertEqual(CountyMenu.CountyMenu(), None)

if __name__ == '__main__':
    unittest.main()
