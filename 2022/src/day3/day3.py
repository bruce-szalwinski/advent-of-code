from more_itertools import chunked

priorities = ".abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def rucksacks():
    with open("input") as file:
        sack = file.readlines()
        return [item.rstrip() for item in sack]


def part1():
    sum_of_priorities = 0
    for s in rucksacks():
        c1 = slice(0, len(s) // 2)
        c2 = slice(len(s) // 2, len(s))

        common = ''.join(
            set(s[c1]).intersection(s[c2])
        )

        sum_of_priorities += list(priorities).index(common)
    return sum_of_priorities


def part2():
    return sum([list(priorities).index(''.join(set(g[0]).intersection(g[1]).intersection(g[2]))) for g in
                chunked(rucksacks(), 3)])


if __name__ == '__main__':
    print(part1())
    print(part2())
