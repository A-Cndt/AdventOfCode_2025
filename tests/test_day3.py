import pytest
import sys

sys.path.append('./')
sys.path.append('../')

from Day3 import part1, part2

INPUT = part1.get_input(3, True)
INPUT2 = part2.get_input(3, True)

def test_day3_part1_example():
    result = part1.solve(INPUT)
    assert result == 357

def test_day3_part2_example():
    result = part2.solve(INPUT2)
    assert result == 3121910778619
