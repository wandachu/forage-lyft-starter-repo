import unittest
from datetime import datetime

from component.tire.carrigan_tire import CarriganTire
from component.tire.octoprime_tire import OctoprimeTire

class TestCarriganTire(unittest.TestCase):
    def test_should_be_serviced(self):
        arr = [0.9, 0.2, 0.1, 0.5]
        carrigan_tire = CarriganTire(arr)
        self.assertTrue(carrigan_tire.needs_service())

    def test_should_not_be_serviced(self):
        arr = [0.8, 0.2, 0.1, 0.5]
        carrigan_tire = CarriganTire(arr)
        self.assertFalse(carrigan_tire.needs_service())


class TestOctoprimeTire(unittest.TestCase):
    def test_should_be_serviced(self):
        arr = [0.7, 0.7, 0.8, 0.8]
        octoprime_tire = OctoprimeTire(arr)
        self.assertTrue(octoprime_tire.needs_service())

    def test_should_not_be_serviced(self):
        arr = [0.7, 0.8, 0.7, 0.7]
        octoprime_tire = OctoprimeTire(arr)
        self.assertFalse(octoprime_tire.needs_service())


if __name__ == '__main__':
    unittest.main()
