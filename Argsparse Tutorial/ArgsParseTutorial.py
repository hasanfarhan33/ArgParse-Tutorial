import math
import argparse

parser = argparse.ArgumentParser(description="Calculate the volume of a Cylinder")
parser.add_argument("-r", "--Radius", type=int, metavar="", required=True, help="Radius of the Cylinder")
parser.add_argument("-H", "--Height", type=int, metavar="", required=True, help="Height of the Cylinder")
args = parser.parse_args()

def cylinder_volume(radius, height):
    volume = (math.pi) * (radius ** 2) * (height)
    return volume

print(cylinder_volume(args.Radius, args.Height))
