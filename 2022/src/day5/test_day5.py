from day5 import relocate_9000, relocate_9001, part2, part1


def test_relocate_9000():
    actual = relocate_9000([1, 2, 3], [4, 5, 6], 1)
    assert actual == ([1, 2], [4, 5, 6, 3])


def test_relocate_9001():
    actual = relocate_9001([1, 2, 3], [4, 5, 6], 2)
    assert actual == ([1], [4, 5, 6, 2, 3])


def test_part1():
    assert "RTGWZTHLD" == part1()

def test_part2():
    assert "STHGRZZFR" == part2()
