"""
Maintainer: Newt
Description: https://adventofcode.com/2019/day/1
"""

def calculate_added_fuel_mass(mass):
    added_fuel = int(mass / 3) - 2

    if added_fuel > 0:
        return added_fuel + calculate_added_fuel_mass(added_fuel)
    else:
        return 0


if __name__ == '__main__':
    print('Starting Day 1 of Advent Calendar')

    sum_of_fuel = 0
    with open('1/day_1_input.txt', 'r') as f:
        line = f.readline()

        while line:
            fuel_needed = int(int(line) / 3) - 2
            sum_of_fuel = sum_of_fuel + fuel_needed + calculate_added_fuel_mass(fuel_needed)
            line = f.readline()

    print('Fuel Required: {}'.format(sum_of_fuel))

