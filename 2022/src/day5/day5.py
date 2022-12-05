def init_stacks():
    return [
    ["N", "C", "R", "T", "M", "Z", "P"],
    ["D", "N", "T", "S", "B", "Z"],
    ["M", "H", "Q", "R", "F", "C", "T", "G"],
    ["G", "R", "Z"],
    ["Z", "N", "R", "H"],
    ["F", "H", "S", "W", "P", "Z", "L", "D"],
    ["W", "D", "Z", "R", "C", "G", "M"],
    ["S", "J", "F", "L", "H", "W", "Z", "Q"],
    ["S", "Q", "P", "W", "N"]
]


def read_directions():
    with open("input") as file:
        lines = file.readlines()
        return [i.rstrip().split(" ") for i in lines]


def relocate_9000(from_stack:list, to_stack: list, num_crates):
    for c in range(0, num_crates):
        to_stack.append(from_stack.pop())

    return from_stack, to_stack


def relocate_9001(from_stack:list, to_stack: list, num_crates):
    crates = []
    for c in range(0, num_crates):
        crates.append(from_stack.pop())

    to_stack.extend(list(reversed(crates)))

    return from_stack, to_stack


def part1():
    directions = read_directions()
    stacks = init_stacks()
    for d in directions:
        num_crates = int(d[1])
        from_stack = int(d[3])-1
        to_stack = int(d[5])-1

        relocate_9000(stacks[from_stack], stacks[to_stack], num_crates)

    return "".join([s.pop() for s in stacks])


def part2():
    directions = read_directions()
    stacks = init_stacks()

    for d in directions:
        num_crates = int(d[1])
        from_stack = int(d[3])-1
        to_stack = int(d[5])-1

        relocate_9001(stacks[from_stack], stacks[to_stack], num_crates)

    return "".join([s.pop() for s in stacks])


if __name__ == '__main__':
    print(part1())
    print(part2())
