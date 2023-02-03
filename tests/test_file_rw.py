"""
Module for file_rw.py tests.
"""
import unittest

import file_rw


class TestFileRW(unittest.TestCase):
    """
    Tests for functions in file_rw.py.
    """

    def test_write(self):
        """
        Assert that write function returns true indicating file found.
        """
        self.assertEqual(file_rw.write("test", "./tests/test_write.json"), True)

    def test_write_filenotfounderror(self):
        """
        Assert that write function raises FileNotFoundError when non-existent
        path is passed as argument.
        """
        with self.assertRaises(FileNotFoundError):
            file_rw.write("test", "./tests/doesnotexist.json")

    def test_read(self):
        """
        Assert that read function returns true indicating file found.
        """
        self.assertEqual(file_rw.read("./tests/test_read.json"), "test read")

    def test_read_filenotfounderror(self):
        """
        Assert that read function raises FileNotFoundError when non-existent
        path is passed as argument.
        """
        with self.assertRaises(FileNotFoundError):
            file_rw.read("./tests/doesnotexist.json")


if __name__ == '__main__':
    unittest.main()
