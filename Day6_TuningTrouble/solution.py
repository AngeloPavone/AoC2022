
def get_input():
    input = []
    with open('test_input', 'r') as f:
        for line in f:
            input.append(line)
    return input

def parse_input(input):
    pass

if __name__ == "__main__":
    parse_input(get_input())
