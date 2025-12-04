import pytest
import sys

sys.path.append('./')
sys.path.append('../')

from Day4 import part1, part2

INPUT = part1.get_input(4, True)
INPUT2 = part2.get_input(4, True)

def test_day4_part1_example():
    result = part1.solve(INPUT)
    assert result == 13

def test_day4_part2_example():
    result = part2.solve(INPUT2)
    assert result == 43
