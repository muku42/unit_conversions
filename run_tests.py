#!/usr/bin/env python

import unittest

from src.convert import kilometers_to_miles, miles_to_kilometers,\
        years_to_minutes, minutes_to_years, joules_to_foe,\
        foe_to_joules

class TestConvert(unittest.TestCase):

    def test_km_to_miles(self):
        actual = kilometers_to_miles(1)
        expected = 0.621 # from google
        self.assertAlmostEqual(actual, expected, delta=0.01)

    def test_miles_to_km(self):
        actual = miles_to_kilometers(1)
        expected = 1.609 # from google
        self.assertAlmostEqual(actual, expected, delta=0.01)

    def test_years_to_minutes(self):
        # Google say there are 525,600 minutes in a year
        self.assertEqual(525600, years_to_minutes(1))

    def test_minutes_to_years(self):
        self.assertEqual(1, minutes_to_years(525600))

    def test_joules_to_foe(self):
        self.assertEqual(1, joules_to_foe(1e44))

    def test_foe_to_joules(self):
        self.assertEqual(1e44, foe_to_joules(1))

########################

if __name__ == '__main__':
    unittest.main()
