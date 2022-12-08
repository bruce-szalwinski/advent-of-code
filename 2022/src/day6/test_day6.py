from day6 import read_input, find_start_of_packet, find_start_of_message


def test_input():
    actual = read_input()
    assert actual[0] == "t"


def test_find_start_of_packet():
    assert find_start_of_packet("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert find_start_of_packet("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert find_start_of_packet("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert find_start_of_packet("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11


def test_find_start_of_message():
    assert find_start_of_message("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
    assert find_start_of_message("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
    assert find_start_of_message("nppdvjthqldpwncqszvftbrmjlhg") == 23
