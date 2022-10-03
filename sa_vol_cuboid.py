#!/usr/bin/env python3
# Created by: Tamer Zreg
# Created on: Oct 3rd, 2022
# This program asks the user for the length, width and height of
# a cuboid in mm. It then calculates and displays
# the volume and surface area using the formulas.


def main():
    # get the length, with and height from the user
    length = float(input("Enter the length of the cuboid (mm): "))
    width = float(input("Enter the width of the cuboid (mm): "))
    height = float(input("Enter the height of the cuboid (mm): "))

    # calculate the surface area and volume
    volume = length * width * height
    surfacearea = 2 * length * width + 2 * length * height + 2 * height * width

    # display the surface area and volume
    print("")
    print("With the length {:,.2f} mm".format(length))
    print("With the width {:,.2f} mm".format(width))
    print("With the height {:,.2f} mm".format(height))
    print("Surface Area = {:,.2f} mm".format(surfacearea))
    print("Circumference = {:,.2f} mm".format(volume))


if __name__ == "__main__":
    main()
