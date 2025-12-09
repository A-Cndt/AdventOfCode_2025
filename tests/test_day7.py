import pytest
import sys

sys.path.append('./')
sys.path.append('../')

from Day7 import part1, part2

INPUT = part1.get_input(7, True)
INPUT2 = part2.get_input(7, True)

def test_day7_part1_example():
    result = part1.solve(INPUT)
    assert result == 21

def test_day7_part2_example():
    result = part2.solve(INPUT2)
    assert result == 40
