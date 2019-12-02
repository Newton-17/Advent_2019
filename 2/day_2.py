"""
Maintainer: Newt
Description: https://adventofcode.com/2019/day/2
"""

import copy

def code_1(input_list, index):
    n1 = input_list[input_list[index+1]]
    n2 = input_list[input_list[index+2]]
    input_list[input_list[index+3]] = n1 + n2
    return input_list, index + 4

def code_2(input_list, index):
    n1 = input_list[input_list[index+1]]
    n2 = input_list[input_list[index+2]]
    input_list[input_list[index+3]] = n1 * n2
    return input_list, index + 4

def update_nv(noun, verb):
    if verb == 99:
        return noun + 1, 1
    else:
        return noun, verb + 1

if __name__ == '__main__':
    print('Starting Day 2 of Advent Calendar')
    with open('2/day_2_input.txt', 'r') as f:
        line = f.read()
        clean_list = [int(x) for x in line.split(',')]
        noun, verb, p0 = 0, -1, 0

        while p0 != 19690720:
            input_list = copy.deepcopy(clean_list)
            index = 0
            cont = True
            noun, verb = update_nv(noun, verb)
            input_list[1] = noun
            input_list[2] = verb

            while cont:
                opcode = input_list[index]
                if opcode == 1:
                    input_list, index = code_1(input_list, index)
                if opcode == 2:
                    input_list, index = code_2(input_list, index)
                if opcode == 99:
                    #print("\nOpcode 99")
                    cont = False
            p0 = input_list[0]
        print((noun*100) + verb)
