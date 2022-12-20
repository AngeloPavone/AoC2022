import re


# TODO: add input array parsing i kinda cheated by putting it in manually
one     = ['r','g','j','b','t','v','z']
two     = ['j','r','v','l']
three   = ['s','q','f']
four    = ['z','h','n','l','f','v','q','g']
five    = ['r','q','t','j','c','s','m','w']
six     = ['s','w','t','c','h','f']
seven   = ['d','z','c','v','f','n','j']
eight   = ['l','g','z','d','w','r','f','q']
nine    = ['j','b','w','v','p']


# test input
# one   = ['z','n']
# two   = ['m','c','d']
# three = ['p']


stacks = {
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine'
}


def move_containers(instructions):
    for instruction in instructions:
        num_of_crates = instruction[0]
        start = eval(stacks[instruction[1]])
        end = eval(stacks[instruction[2]])

        try:
            count = 0
            while count < num_of_crates:
                current_crate = start.pop()
                end.append(current_crate)
                count += 1
        except Exception as e: print(e)

    return stacks

def parse_input():
    with open('input', 'r') as f:
        lines = f.readlines()

    # parse input to remove all none numbers and conver the numbers to int
    instructions = []
    for instruction in lines:
        instruction = re.split('move | from | to |\n', instruction)
        while '' in instruction:
            instruction.remove('')
        instructions.append([eval(i) for i in instruction])

    return instructions

if __name__ == '__main__':
    for i in move_containers(parse_input()):
        print(eval(stacks[i])[-1], end='')
