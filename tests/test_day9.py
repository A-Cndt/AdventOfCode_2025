import pytest
import sys

sys.path.append('./')
sys.path.append('../')

from Day9 import part1, part2

INPUT = part1.get_input(9, True)
INPUT2 = part2.get_input(9, True)

def test_day9_part1_example():
    result = part1.solve(INPUT)
    assert result == 50

def test_day9_part2_example():
    result = part2.solve(INPUT2)
    assert result == 24
