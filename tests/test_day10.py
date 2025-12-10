import pytest
import sys

sys.path.append('./')
sys.path.append('../')

from Day10 import part1, part2

INPUT = part1.get_input(10, True)
INPUT2 = part2.get_input(10, True)

def test_day10_part1_example():
    result = part1.solve(INPUT)
    assert result == 7

def test_day10_part2_example():
    result = part2.solve(INPUT2)
    assert result == 33
