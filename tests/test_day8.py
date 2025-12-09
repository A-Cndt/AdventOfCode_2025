import pytest
import sys

sys.path.append('./')
sys.path.append('../')

from Day8 import part1, part2

INPUT = part1.get_input(8, True)
INPUT2 = part2.get_input(8, True)

def test_day8_part1_example():
    result = part1.solve(INPUT, 10)
    assert result == 40

def test_day8_part2_example():
    result = part2.solve(INPUT2)
    assert result == 25272
