"""
Maintainer: Newt
Description: https://adventofcode.com/2019/day/2
"""

import sys
import time

import networkx as nx

    

if __name__ == '__main__':
    start_time = time.time()
    print('Starting Day 8 of Advent Calendar')

    HEIGHT = 25
    WIDTH = 6
    n = HEIGHT * WIDTH
    with open("data.txt", 'r') as f:
        line = f.read().strip()
        
        layers = [line[i:i+n] for i in range(0, len(line), n)]

        fewest_count = 1000000000000000
        fewest_layer = []
        for layer in layers:
            new_layer_count = layer.count('0')
            if new_layer_count < fewest_count:
                fewest_count = new_layer_count
                fewest_layer = layer

        
        num_1 = fewest_layer.count('1')
        num_2 = fewest_layer.count('2')

        print('num_1 * num_2 = {}'.format(num_1*num_2))
    
    print("--- %s seconds ---" % (time.time() - start_time))
    
    
