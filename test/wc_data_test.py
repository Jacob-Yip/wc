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

    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_invalid_constructor(self):
        pass

    def test_equal(self):
        for test_data_set in WCDataTest.TEST_EQUAL_TEST_VALUES:
            self.assertEqual(
                test_data_set[2], (test_data_set[0] == test_data_set[1]))

    def test_str(self):
        pass

    def test_property(self):
        pass
