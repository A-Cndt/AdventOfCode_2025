import pytest
import sys

sys.path.append('./')
sys.path.append('../')

from Day12 import answer

INPUT = answer.get_input(12, True)

def test_day12():
    result = answer.solve(INPUT)
    assert result == 2
