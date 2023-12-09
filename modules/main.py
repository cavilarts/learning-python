# import dog imports everything
import sys
import argparse
from math import sqrt
from lib.dog import bark

bark()

print(sqrt(3))
print(sys.argv)

parser = argparse.ArgumentParser(
  description="This program prints a color name"
)

parser.add_argument("-c", "--color", metavar="color", required=True, help="the color to search for")

args = parser.parse_args() 

print(args.color)