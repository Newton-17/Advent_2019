"""
Maintainer: Newt
Description: https://adventofcode.com/2019/day/2
"""

from collections import Counter 
import time

def check(n):
    if check_lowest(n):
        # Day 1 Part 1 - replace line 12 w/ atleast_doubles(n)
        return only_doubles(n)
    return False

def check_lowest(n):
    lowest = 1
    for i in range(0, len(n)):
        if int(n[i]) < lowest:
            return False
        lowest = int(n[i])
    return True

def atleast_doubles(n):
    for i in range(0, len(n) - 1):
        if n[i] == n[i + 1]:
            return True
    return False

def only_doubles(n):
    count = Counter(n)
    for i in range(1, 10):
        if count[str(i)] == 2:
            return True
    return False

# Looking at a way to walk-through to get the next lowest-abiding number
def update_i(i):
    i = str(i)

    if int(i[0]) < int(i[1]):
        i[0] = str(int(i[0]) + 1)
        for x in range(1, len(i)):
            i[x] = '0'
            return int(i)
    else:
        return i+1

    

if __name__ == '__main__':
    start_time = time.time()
    print('Starting Day 4 of Advent Calendar')

    count = 0
    i = 193651
    while i <= 649729:
        if check(str(i)):
            count += 1
            i = update_i(i)

    print(count)
    print("--- %s seconds ---" % (time.time() - start_time))
    