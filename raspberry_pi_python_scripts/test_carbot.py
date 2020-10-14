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

    def test_key_controller_with_wrong_string(self):
        print("testing key_controller()...")
        key_press = "R"
        result = self.carbot.key_controller(key_press)
        expected_result = None
        self.assertEqual(result, expected_result)

    def test_key_controller_with_keypress_w(self):
        print("testing key_controller()...")
        key_press = "w"
        result = self.carbot.key_controller(key_press)
        expected_result = None
        self.assertEqual(result, expected_result)

    def test_key_controller_with_keypress_z(self):
        print("testing key_controller()...")
        key_press = "z"
        result = self.carbot.key_controller(key_press)
        expected_result = None
        self.assertEqual(result, expected_result)

    def test_key_controller_with_keypress_a(self):
        print("testing key_controller()...")
        key_press = "a"
        result = self.carbot.key_controller(key_press)
        expected_result = None
        self.assertEqual(result, expected_result)

    def test_key_controller_with_keypress_s(self):
        print("testing key_controller()...")
        key_press = "s"
        result = self.carbot.key_controller(key_press)
        expected_result = None
        self.assertEqual(result, expected_result)

    def test_key_controller_with_keypress_q(self):
        print("testing key_controller()...")
        key_press = "q"
        result = self.carbot.key_controller(key_press)
        expected_result = None
        self.assertEqual(result, expected_result)



if __name__ == "__main__":
    unittest.main()
