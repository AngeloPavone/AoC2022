import re

one     =       ['n','z']
two     =       ['d','c','m']
three   =       ['p']


def parse_input():
    with open('small_input', 'r') as f:
        lines = f.readlines()

# parse input to remove all none numbers and conver the numbers to int
    instructions = []
    for instruction in lines:
        instruction = re.split('move | from | to |\n', instruction)
        instruction = instruction[1:-1]
        instructions = [eval(i) for i in instruction]

        print(instructions)

if __name__ == '__main__':
    parse_input()
