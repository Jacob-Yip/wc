import unittest
from main.wc_data import WCData


class WCDataTest(unittest.TestCase):
    DUMMY_FILE_PATH_1 = "resource/test/test_equal_1.txt"
    DUMMY_FILE_PATH_2 = "resource/test/test_equal_2.txt"
    TEST_EQUAL_TEST_VALUES = [  # In the form of [First instance, Second instance, boolean equal?]
        [WCData(1, 1, 1, DUMMY_FILE_PATH_1), WCData(
            1, 1, 1, DUMMY_FILE_PATH_1), True],
        [WCData(1, 1, 1, DUMMY_FILE_PATH_2), WCData(
            1, 1, 1, DUMMY_FILE_PATH_2), True],
        [WCData(10, 1, 1, DUMMY_FILE_PATH_1), WCData(
            1, 1, 1, DUMMY_FILE_PATH_1), False],
        [WCData(1, 10, 1, DUMMY_FILE_PATH_1), WCData(
            1, 1, 1, DUMMY_FILE_PATH_1), False],
        [WCData(1, 1, 10, DUMMY_FILE_PATH_1), WCData(
            1, 1, 1, DUMMY_FILE_PATH_1), False],
        [WCData(10, 10, 1, DUMMY_FILE_PATH_1), WCData(
            1, 1, 1, DUMMY_FILE_PATH_1), False],
        [WCData(10, 1, 10, DUMMY_FILE_PATH_1), WCData(
            1, 1, 1, DUMMY_FILE_PATH_1), False],
        [WCData(1, 10, 10, DUMMY_FILE_PATH_1), WCData(
            1, 1, 1, DUMMY_FILE_PATH_1), False],
        [WCData(10, 10, 10, DUMMY_FILE_PATH_1), WCData(
            1, 1, 1, DUMMY_FILE_PATH_1), False],
        [WCData(10, 10, 10, DUMMY_FILE_PATH_1), None, False]
    ]
    TEST_STR_TEST_VALUES = {  # In the form of expected name, WCData instance
        f"LINE_COUNT  WORD_COUNT  BYTE_COUNT  FILE_PATH\n1    2    3    {DUMMY_FILE_PATH_1}": WCData(1, 2, 3, DUMMY_FILE_PATH_1),
        f"LINE_COUNT  WORD_COUNT  BYTE_COUNT  FILE_PATH\n10    20    30    {DUMMY_FILE_PATH_1}": WCData(10, 20, 30, DUMMY_FILE_PATH_1),
        f"LINE_COUNT  WORD_COUNT  BYTE_COUNT  FILE_PATH\n100    200    300    {DUMMY_FILE_PATH_2}": WCData(100, 200, 300, DUMMY_FILE_PATH_2),
        f"LINE_COUNT  WORD_COUNT  BYTE_COUNT  FILE_PATH\n1000    2000    3000    {DUMMY_FILE_PATH_2}": WCData(1000, 2000, 3000, DUMMY_FILE_PATH_2)
    }
    TEST_PROPERTY_TEST_VALUES = [  # In the form of [instance, line_count, word_count, byte_count, file_path]
        [WCData(1, 2, 3, DUMMY_FILE_PATH_1), 1, 2, 3, DUMMY_FILE_PATH_1],
        [WCData(2, 4, 8, DUMMY_FILE_PATH_2), 2, 4, 8, DUMMY_FILE_PATH_2]
    ]

    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def suite(self) -> None:
        suite = unittest.TestSuite()

        # Add unit tests to test suite
        suite.addTest(WCDataTest("test_invalid_constructor"))
        suite.addTest(WCDataTest("test_equal"))
        suite.addTest(WCDataTest("test_str"))
        suite.addTest(WCDataTest("test_property"))

        return suite

    def test_invalid_constructor(self):
        # Absence of parameter(s)
        with self.assertRaises(Exception):
            _ = WCData(None, 0, 0, WCDataTest.DUMMY_FILE_PATH_1)

        with self.assertRaises(Exception):
            _ = WCData(0, None, 0, WCDataTest.DUMMY_FILE_PATH_1)

        with self.assertRaises(Exception):
            _ = WCData(0, 0, None, WCDataTest.DUMMY_FILE_PATH_1)

        with self.assertRaises(Exception):
            _ = WCData(0, 0, 0, None)

        # Invalid parameter type(s)
        with self.assertRaises(Exception):
            _ = WCData("str", 0, 0, WCDataTest.DUMMY_FILE_PATH_1)

        with self.assertRaises(Exception):
            _ = WCData(0, "str", 0, WCDataTest.DUMMY_FILE_PATH_1)

        with self.assertRaises(Exception):
            _ = WCData(0, 0, "str", WCDataTest.DUMMY_FILE_PATH_1)

        with self.assertRaises(Exception):
            _ = WCData(0, 0, 0, -1)

        # Invalid parameter values
        with self.assertRaises(Exception):
            _ = WCData(-1, 0, 0, WCDataTest.DUMMY_FILE_PATH_1)

        with self.assertRaises(Exception):
            _ = WCData(0, -1, 0, WCDataTest.DUMMY_FILE_PATH_1)

        with self.assertRaises(Exception):
            _ = WCData(0, 0, -1, WCDataTest.DUMMY_FILE_PATH_1)

        with self.assertRaises(Exception):
            _ = WCData(0, 0, 0, "non-existent file")

        # Normal case
        _ = WCData(0, 0, 0, WCDataTest.DUMMY_FILE_PATH_1)

    def test_equal(self):
        for test_data_set in WCDataTest.TEST_EQUAL_TEST_VALUES:
            self.assertEqual(
                test_data_set[2], (test_data_set[0] == test_data_set[1]))

    def test_str(self):
        for (expected_str, instance) in WCDataTest.TEST_STR_TEST_VALUES.items():
            print(instance)
            self.assertEqual(expected_str, str(instance))

    def test_property(self):
        for test_data_set in WCDataTest.TEST_PROPERTY_TEST_VALUES:
            self.assertEqual(test_data_set[1], test_data_set[0].line_count)
            self.assertEqual(test_data_set[2], test_data_set[0].word_count)
            self.assertEqual(test_data_set[3], test_data_set[0].byte_count)
            self.assertEqual(test_data_set[4], test_data_set[0].file_path)


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    wc_data_tester = WCDataTest()
    runner.run(wc_data_tester.suite())
