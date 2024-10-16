'''
    Find the average of all runs scored by a player
'''

import sys
filename = sys.argv[1]
with open(filename) as FH:
    total = 0
    count = 0
    for line in FH:
        #print(line, end="")
        total =+ int(line)
        #print(f'{total =}')
        count =+ 1

print("Average", total/count)
