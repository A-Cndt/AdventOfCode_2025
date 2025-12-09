import pytest
import sys

sys.path.append('./')
sys.path.append('../')

from Day6 import part1, part2

INPUT = part1.get_input(6, True)
INPUT2 = part2.get_input(6, True)

def test_day6_part1_example():
    result = part1.solve(INPUT)
    assert result == 4277556

def test_day6_part2_example():
    result = part2.solve(INPUT2)
    assert result == 3263827
