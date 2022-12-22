def get_input():
    with open('input', 'r') as f:
        input = f.readlines()
        result = input[0]
    return result

def parse_input(input):
    buffer = []
    fuckme = set()

    for char in range(len(input) - 3):
        buffer.extend(input[char:char + 4])
        try:
            for char1 in buffer:
                fuckme.add(char1)
            if len(fuckme) == 4:
                return char + 4
            else:
                fuckme.clear()
        except:
            pass
        buffer.clear()


if __name__ == "__main__":
    print(parse_input(get_input()))
