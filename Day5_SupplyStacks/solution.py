import re

one     =       ['n','z']
two     =       ['d','c','m']
three   =       ['p']


with open('small_input', 'r') as f:
    lines = f.readlines()

    # parse input to remove all none numbers so that i can easily reference them
    for instruction in lines:
        instruction = re.split('move | from | to |\n', instruction) # can problem use re.search()
        instruction = instruction[1:-1]
