import pytest
from project import simulate, get_max_height

def test_simulate_history():
    history = simulate(50, 45, 0.145, 0, 0.00426)
    assert len(history) > 0

def test_land_pos():
    history = simulate(50, 45, 0.145, 0, 0.00426)
    assert history[-1].y < 0 

def test_get_max_height():
    history = simulate(50, 45, 0.145, 0, 0.00426)
    assert round(get_max_height(history), 1) == 63.5  # known value