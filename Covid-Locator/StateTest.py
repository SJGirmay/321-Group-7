import unittest
from unittest.mock import patch

import StateMenu
from Parser import jprint, stateDataPrint

#resp = input('Invalid Input. Please Enter valid State or State Abreviation or q/quit ')
#removed because recursion limit

class TestState(unittest.TestCase):

    @patch('builtins.input', side_effect=['VA'])
    def test_State1(self, mock_inputs):
        result=StateMenu.StateMenu()
        self.assertEqual(result, 'Success')

    @patch('builtins.input', side_effect=['Virginia'])
    def test_State2(self, mock_inputs):
        result=StateMenu.StateMenu()
        self.assertEqual(result, 'Success')

    @patch('builtins.input', side_effect=['virginia'])
    def test_State3(self, mock_inputs):
        result=StateMenu.StateMenu()
        self.assertEqual(result, 'Success')

    @patch('builtins.input', side_effect=['Maryland'])
    def test_State4(self, mock_inputs):
        result=StateMenu.StateMenu()
        self.assertEqual(result, 'Success')

    @patch('builtins.input', side_effect=['MD'])
    def test_State5(self, mock_inputs):
        result=StateMenu.StateMenu()
        self.assertEqual(result, 'Success')

    @patch('builtins.input', side_effect=['Virrr'])
    def test_State6(self, mock_inputs):
        result=StateMenu.StateMenu()
        self.assertEqual(result, 0)

    @patch('builtins.input', side_effect=['MDland'])
    def test_State7(self, mock_inputs):
        result=StateMenu.StateMenu()
        self.assertEqual(result, 0)

    @patch('builtins.input', side_effect=['Canadaa'])
    def test_State8(self, mock_inputs):
        result=StateMenu.StateMenu()
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()