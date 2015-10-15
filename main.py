#!/usr/bin/env python

# Command line script to convert a single number to an from several units

import argparse

from src.convert import kilometers_to_miles, miles_to_kilometers,\
        years_to_minutes, minutes_to_years, joules_to_foe,\
        foe_to_joules

# Parse command line args
parser = argparse.ArgumentParser()
parser.add_argument('value', type=float, help="The number to be converted")
args = parser.parse_args()

# Perform conversions
# km to miles
to_miles = kilometers_to_miles(args.value)
print("{0} kilometers is {1} miles".format(args.value, to_miles))

# miles to km
to_km = miles_to_kilometers(args.value)
print("{0} miles is {1} kilomters".format(args.value, to_km))

# years to minutes
to_minutes = years_to_minutes(args.value)
print("{0} years is {1} minutes".format(args.value, to_minutes))

# minutes to years
to_years = minutes_to_years(args.value)
print("{0} minutes is {1} years".format(args.value, to_years))

# joules to foe
to_foe = joules_to_foe(args.value)
print("{0} joules is {1} foe".format(args.value, to_foe))

# foe to joules
to_joules = foe_to_joules(args.value)
print("{0} foe is {1} joules".format(args.value, to_joules))
