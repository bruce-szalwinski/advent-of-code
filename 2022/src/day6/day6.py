from more_itertools import windowed


def read_input():
    with open("input") as file:
        return file.readline()


def find_marker(dstream: str, unique_characters):
    for w in windowed(dstream, unique_characters):
        if len(set(w)) == unique_characters:
            return dstream.index(''.join(w)) + unique_characters


def find_start_of_packet(dstream: str):
    return find_marker(dstream, 4)


def find_start_of_message(dstream: str):
    return find_marker(dstream, 14)


def part1():
    return find_start_of_packet(read_input())


def part2():
    return find_start_of_message(read_input())


if __name__ == '__main__':
    print(part1())
    print(part2())
