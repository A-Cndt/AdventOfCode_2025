import pytest
import sys

sys.path.append('./')
sys.path.append('../')

from Day2 import part1, part2

INPUT = part1.get_input(2, True)

def test_solve_example():
    result_p1 = part1.solve(INPUT)
    result_p2 = part2.solve(INPUT, 2)
    
    assert result_p1 == 1227775554
    assert result_p2 == 4174379265
    
def test_day2_part1_example():
    result = part1.solve(INPUT)
    assert result == 1227775554

def test_day2_part2_example():
    result = part2.solve(INPUT, 2)
    assert result == 4174379265
