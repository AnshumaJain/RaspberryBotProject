import sys
import mock
import unittest

sys.modules['RPi.GPIO'] = mock.MagicMock()
sys.modules['RPi'] = mock.MagicMock()

from carbot import CarBot


class TestCarBot(unittest.TestCase):
    carbot = CarBot()

    def test_forward(self):
        print("testing forward()...")
        result = self.carbot.forward()
        expected_result = None
        self.assertEqual(result, expected_result)

    def test_reverse(self):
        print("testing reverse()...")
        result = self.carbot.reverse()
        expected_result = None
        self.assertEqual(result, expected_result)

    def test_turn_right(self):
        print("testing turn_right()...")
        result = self.carbot.turn_right()
        expected_result = None
        self.assertEqual(result, expected_result)

    def test_stop_car(self):
        print("testing stop_car()...")
        result = self.carbot.stop_car()
        expected_result = None
        self.assertEqual(result, expected_result)

    def test_turn_left(self):
        print("testing turn_left()...")
        result = self.carbot.turn_left()
        expected_result = None
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
