"""
Maintainer: Newt
Description: https://adventofcode.com/2019/day/2
"""

import time

import networkx as nx

    

if __name__ == '__main__':
    start_time = time.time()
    print('Starting Day 6 of Advent Calendar')

    print('Creating Empty Graph')
    #g = nx.DiGraph() - Commented out because its not needed in part 2
    g = nx.Graph() 
    with open("data_6.txt", 'r') as f:
        line = f.readline().strip()
        while line:
            # split line
            u, v = line.split(")")
            # Add Edge
            g.add_edge(v, u)
            # Read next line
            line = f.readline().strip()
            
    
    # Start from Source & count 

    #print(nx.find_cycle(g))

    """
    # Commented out, not needed in part 2
    count = 0
    final_paths = []
    for u in g.nodes():
        longest_path = []
        for i in g.nodes():
            try:
                path = nx.shortest_path(g, u, i)
                if len(path) > len(longest_path):
                    longest_path = path
            except:
                pass
        if len(longest_path) > 1:
            final_paths.append(longest_path)

    
    for path in final_paths:
        count += len(path) - 1
        print(path)
    """

    path = nx.shortest_path(g, "YOU", "SAN")
    print(path)

    # Answer is path minus 3 for SAN, YOU, and the last node
    print(len(path) - 3) 
    
    print("--- %s seconds ---" % (time.time() - start_time))
    
    
