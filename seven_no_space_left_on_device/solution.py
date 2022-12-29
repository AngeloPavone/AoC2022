INPUT_FILE = 'input'


class Node:
    def __init__(self, data: int):
        self.data = data
        self.children = []


    def insert(self, node: object):
        self.children.append(node)


def parse_file(input: str):
    with open(input, 'r') as f:
        lines = f.readlines()
        for line in range(len(lines)):
            lines[line] = lines[line].strip()
        return lines



if __name__ == '__main__':
    print(parse_file(INPUT_FILE))
