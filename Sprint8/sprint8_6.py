import unittest
import os
from unittest.mock import Mock
from unittest.mock import mock_open
from unittest.mock import patch
import builtins


def count_str(file, str):
    with open(file, 'r') as f:
        occur = f.read().count(str)
    return occur

def file_parser(file, *args):
    if len(args)==1:
        return f"Found {count_str(file, args[0])} strings"
    elif len(args)==2:
        occur = count_str(file, args[0])
        with open(file, 'r') as f:
            new_text=f.read().replace(args[0], args[1])
        with open(file, 'w') as f:
            f.write(new_text)
        return f"Replaced {occur} strings"


class ParserTest(unittest.TestCase):

    def test_file_parser_one_arg(self):
        with patch('builtins.open', mock_open(read_data='Hello world!')) as m:
            actual = file_parser("file.txt", "o")
            expected = "Found 2 strings"
            self.assertEqual(actual, expected)

    def test_file_parser_two_arg(self):
        with patch('builtins.open', mock_open(read_data='Hello world!')) as m:
            actual = file_parser("file.txt", "l", "L")
            expected = "Replaced 3 strings"
            self.assertEqual(actual, expected)
        m().write.assert_called_once_with('HeLLo worLd!')


if __name__ == '__main__':
    unittest.main()


file1=os.path.dirname(__file__) + "\\files\\file1.txt"
print(file_parser(file1, 'o'))
print(file_parser(file1, 'x', 'o'))
