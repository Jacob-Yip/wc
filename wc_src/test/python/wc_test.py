"""
Unit test for WC in main.wc
"""

import unittest
from wc_src.main.python.wc import WC
import os
from wc_src.main.python.wc_data import WCData


class WCTest(unittest.TestCase):
    TEST_GET_WC_TEST_VALUES = {  # In the form of {filename: expected WCData instance}
        "wc_src/test/resource/test_get_wc_0_0_0.txt": WCData(
            0, 0, 0, "wc_src/test/resource/test_get_wc_0_0_0.txt"),
        "wc_src/test/resource/test_get_wc_1_176_1142.txt": WCData(
            1, 176, 1142, "wc_src/test/resource/test_get_wc_1_176_1142.txt"),
        "wc_src/test/resource/test_get_wc_10_0_60.txt": WCData(
            10, 0, 60, "wc_src/test/resource/test_get_wc_10_0_60.txt"),
        "wc_src/test/resource/test_get_wc_14_0_28.txt": WCData(
            14, 0, 28, "wc_src/test/resource/test_get_wc_14_0_28.txt")
    }

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
        suite.addTest(WCTest("test_get_wc"))

        return suite

    def test_valid_file_path(self):
        """
        Test whether wc accepts valid file path
        """
        FILE_PATH = "wc_src/test/resource/test_valid_file_path.txt"
        file_content = "First line\n" + \
            "2nd line\n" + \
            "3rd line\n" + \
            "There should be 6 lines\n" + \
            "Thus, the result should be 6    23    160    wc_src/test/resource/test_valid_file_path.txt\n" + \
            "End of file"

        new_file = None
        try:
            # Create a file
            new_file = open(FILE_PATH, "wt")
            new_file.write(file_content)
            new_file.flush()

            expected_wc_data = WCData(
                line_count=6,
                word_count=23,
                byte_count=160,
                file_path=FILE_PATH
            )

            wc = WC(file_path=FILE_PATH)
            wc_data = wc.get_wc()

            self.assertEqual(first=expected_wc_data, second=wc_data)
        except Exception as e:
            self.fail()
        finally:
            if not new_file is None:
                new_file.close()

            # We have to close the process new_file first before using os
            # Delete the newly created file
            if os.path.exists(FILE_PATH):
                os.remove(FILE_PATH)

    def test_invalid_file_path(self):
        """
        Test whether wc throws Exception when invalid file paths are given
        """
        # Non-existent file path
        with self.assertRaises(Exception):
            _ = WC(file_path="xxxxxx")

        # Empty file path
        with self.assertRaises(Exception):
            _ = WC(file_path="")

        # Not supplying any file path
        with self.assertRaises(Exception):
            _ = WC()

        # Invalid file format
        with self.assertRaises(Exception):
            _ = WC(file_path="-")

        # Invalid file extension
        with self.assertRaises(Exception):
            _ = WC(file_path="xxx.md")

    def test_get_wc(self):
        """
        Test the result of get_wc() in WC
        Since it is not possible to implement all possible file combinations, I used input partitions to test different types of files
        """
        for (file_path, expected_instance) in WCTest.TEST_GET_WC_TEST_VALUES.items():
            wc = WC(file_path=file_path)
            actual_instance = wc.get_wc()
            self.assertEqual(expected_instance, actual_instance)


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    wc_tester = WCTest()
    runner.run(wc_tester.suite())
