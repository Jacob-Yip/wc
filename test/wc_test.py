"""
Unit test for WC in main.wc
"""

import unittest
from main.wc import WC
import os
from main.wc_data import WCData


class WCTest(unittest.TestCase):
    def setUp(self) -> None:
        # We will not create the wc instance here because each wc instance in each unit test is different due to file_path
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def suite(self) -> None:
        suite = unittest.TestSuite()

        # Add unit tests to test suite
        suite.addTest(WCTest("test_valid_file_path"))
        suite.addTest(WCTest("test_invalid_file_path"))

        return suite

    def test_valid_file_path(self):
        FILE_PATH = "resource/test/test_valid_file_path.txt"
        file_content = "First line\n" + \
            "2nd line\n" + \
            "3rd line\n" + \
            "There should be 6 lines\n" + \
            "Thus, the result should be 6    23    153    resource/test/test_valid_file_path.txt\n" + \
            "End of file"

        try:
            # Create a file
            new_file = open(FILE_PATH, "wt")
            new_file.write(file_content)
            new_file.flush()

            expected_wc_data = WCData(
                line_count=6,
                word_count=23,
                byte_count=153,
                file_path=FILE_PATH
            )

            wc = WC(file_path=FILE_PATH)
            wc_data = wc.get_wc()

            self.assertEqual(first=expected_wc_data, second=wc_data)
        except Exception as e:
            self.fail()
        finally:
            new_file.close()

            # We have to close the process new_file first before using os
            # Delete the newly created file
            if os.path.exists(FILE_PATH):
                os.remove(FILE_PATH)

    def test_invalid_file_path(self):
        # Non-existent file path
        with self.assertRaises(Exception):
            self.__wc = WC(file_path="xxxxxx")

        # Empty file path
        with self.assertRaises(Exception):
            self.__wc = WC(file_path="")

        # Not supplying any file path
        with self.assertRaises(Exception):
            self.__wc = WC()

        # Invalid file format
        with self.assertRaises(Exception):
            self.__wc = WC(file_path="-")


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    wc_tester = WCTest()
    runner.run(wc_tester.suite())
