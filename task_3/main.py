import unittest
import math


def time_to_cyclic_feature(time: float):
    """
    Convert time (in hours) to a cyclic feature using sine and cosine.

    Args:
        time (float): Time in hours (0 <= time < 24)

    Returns:
        tuple: (sin_time, cos_time)
    """
    if time < 0 or time >= 24:
        raise ValueError("Time should be between 0 and 24 hours.")

    # Convert time to radians (0 - 2pi)
    angle = (2 * math.pi * time) / 24.0
    sin_time = math.sin(angle)
    cos_time = math.cos(angle)

    return sin_time, cos_time


def time_difference_in_hours(start: float, end: float) -> float:
    """
    Calculate the time difference between two times, correctly handling the cyclic nature of time.

    Args:
        start (float): Start time in hours (0 <= start < 24)
        end (float): End time in hours (0 <= end < 24)

    Returns:
        float: Time difference in hours (always positive and between 0 and 12 hours)
    """
    if start < 0 or start >= 24 or end < 0 or end >= 24:
        raise ValueError("Time should be between 0 and 24 hours.")

    # Calculate the raw difference
    diff = (end - start) % 24

    # If the difference is greater than 12 hours, we should take the other direction around the clock
    if diff > 12:
        diff = 24 - diff

    return diff


class TestTimeConversion(unittest.TestCase):

    def test_time_to_cyclic_feature(self):
        self.assertAlmostEqual(time_to_cyclic_feature(0)[0], 0.0)
        self.assertAlmostEqual(time_to_cyclic_feature(0)[1], 1.0)
        self.assertAlmostEqual(time_to_cyclic_feature(6)[0], 1.0)
        self.assertAlmostEqual(time_to_cyclic_feature(6)[1], 0.0)
        self.assertAlmostEqual(time_to_cyclic_feature(12)[0], 0.0)
        self.assertAlmostEqual(time_to_cyclic_feature(12)[1], -1.0)
        self.assertAlmostEqual(time_to_cyclic_feature(18)[0], -1.0)
        self.assertAlmostEqual(time_to_cyclic_feature(18)[1], 0.0)
        self.assertAlmostEqual(time_to_cyclic_feature(23)[0], math.sin(2 * math.pi * 23 / 24))
        self.assertAlmostEqual(time_to_cyclic_feature(23)[1], math.cos(2 * math.pi * 23 / 24))

    def test_time_difference_in_hours(self):
        self.assertEqual(time_difference_in_hours(23, 1), 2)
        self.assertEqual(time_difference_in_hours(0, 12), 12)
        self.assertEqual(time_difference_in_hours(6, 18), 12)
        self.assertEqual(time_difference_in_hours(18, 6), 12)
        self.assertEqual(time_difference_in_hours(23, 23), 0)
        self.assertEqual(time_difference_in_hours(1, 23), 2)
        self.assertEqual(time_difference_in_hours(5, 20), 9)  # Fixed this expected value to 9

    def test_invalid_time(self):
        with self.assertRaises(ValueError):
            time_to_cyclic_feature(24)  # Invalid time
        with self.assertRaises(ValueError):
            time_to_cyclic_feature(-1)  # Invalid time
        with self.assertRaises(ValueError):
            time_difference_in_hours(24, 12)  # Invalid time
        with self.assertRaises(ValueError):
            time_difference_in_hours(-1, 12)  # Invalid time


if __name__ == '__main__':
    unittest.main()
