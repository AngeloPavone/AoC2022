INPUT_FILE = 'test'


class Node:
    def __init__(self, dir: str):
        self.data = 0
        self.dir = dir
        self.children = []


    def add_node(self, name: object):
        self.children.append(name)


    def add_dir(self, dir: str):
        self.dir = dir


    def get_children(self):
        return self.children


    def get_dir(self):
        return self.dir


def parse_file(input: str) -> list:
    with open(input, 'r') as f:
        lines = f.readlines()
        for line in range(len(lines)):
            lines[line] = lines[line].strip()
        return lines

def parse_input(lines: list):
    head = Node('/')
    for command in range(len(lines)):
        if lines[command] == '$ ls':
            new_node = Node(lines[command+1])
            head.add_node(new_node)
            for next_command in range(command+1, len(lines)):
                if lines[next_command].startswith('$'):
                    break
                print(lines[next_command])
            print()

    return head


def print_nodes(head: Node) -> None:
    for child in head.get_children():
        print(child.get_dir())


def main():
    head = parse_input(parse_file(INPUT_FILE))
    print_nodes(head)


if __name__ == '__main__':
    main()
