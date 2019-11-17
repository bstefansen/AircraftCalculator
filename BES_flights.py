# Filename: BES_flights.py
# Author: Blake Stefansen
# Description: A program that calculates the amount of time and fuel for a 1980 Cessna 172N to fly a specified distance.

import time

def intro():
    print()
    print("Aircraft Fuel Calculator")
    print()

def flight(distance):
    flight = distance / 120
    return flight

def hflight(distance):
    flight = distance / 120
    hflight, mflight = divmod(flight, 1)
    return int(hflight)

def mflight(distance):
    flight = distance / 120
    hflight, mflight = divmod(flight, 1)
    mflight = mflight * 60
    return int(mflight)

def fuel(distance):
    fuel = 8.4*(flight(distance)+0.5)
    fuel = round(fuel, 1)
    return fuel

def output(distance):
    print()
    print("Flight time: " + (str(hflight(distance))) + " hour(s) and " + (str(mflight(distance))) + " minutes")
    print("Required fuel: " + (str(fuel(distance))) + " gallons")
    print()

def again():
    redo = input("Continue? (y/n): ")
    if redo == "n":
        print()
        print("Bye!")
    elif redo == "y":
        main()
    else:
        print("Sorry, try again...")
        time.sleep(1)
        print()
        again()

def main():
    intro()
    distance = float(input(("Distance in nautical miles: ")))
    flight(distance)
    fuel(distance)
    output(distance)
    again()

if __name__ == '__main__':
    main()