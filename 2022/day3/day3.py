
priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def rucksacks():
    with open("input") as file:
        line_list = file.readlines()
        return [item.rstrip() for item in line_list]


def part1():
    sum_of_priorities = 0
    sacks = rucksacks()
    for s in sacks:
        c1 = slice(0, len(s) // 2)
        c2 = slice(len(s) // 2, len(s))

        common = ''.join(
            set(s[c1]).intersection(s[c2])
        )

        sum_of_priorities += list(priorities).index(common) + 1
    print(sum_of_priorities)


def part2():
    sum_of_priorities = 0

    sacks = rucksacks()
    groups = []
    i = 1
    for s in sacks:
        if len(groups) == i:
            groups[i-1].append(s)
        else:
            groups.append([s])

        if sacks.index(s) % 3 == 2:
            i += 1

    for g in groups:
        common = ''.join(set(g[0]).intersection(g[1]).intersection(g[2]))
        sum_of_priorities += list(priorities).index(common) + 1

    print(sum_of_priorities)



if __name__ == '__main__':
    #part1()
    part2()

