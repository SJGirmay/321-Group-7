import unittest
from unittest.mock import patch

import NationalMenu
from Parser import jprint, nationalDataPrint

#from flask import Flask, render_template, request
#app = Flask(__name__)

class TestState(unittest.TestCase):

    @patch('builtins.input', side_effect=[])
    def test_National1(self, mock_inputs):
        result=NationalMenu.NationalMenu()
        self.assertEqual(result, 'Success')


if __name__ == '__main__':
    unittest.main()