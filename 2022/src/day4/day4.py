def assignments():
    with open("input") as file:
        pairs = file.readlines()
        return [pair.rstrip().split(",") for pair in pairs]


def to_set(r: str):
    start, finish = r.split("-")
    if start == finish:
        return {int(start)}
    else:
        return set(range(int(start), int(finish) + 1, 1))


def is_superset(a: set, b: set):
    return a.issuperset(b) or b.issuperset(a)


def is_intersect(a: set, b: set):
    return len(a.intersection(b))


def part1():
    return sum([1 if (is_superset(to_set(a[0]), to_set(a[1])) or is_superset(to_set(a[1]), to_set(a[0]))) else 0 for a in assignments()])


def part2():
    return sum([1 if is_intersect(to_set(a[0]), to_set(a[1])) else 0 for a in assignments()])


if __name__ == '__main__':
    print(part1())
    print(part2())
