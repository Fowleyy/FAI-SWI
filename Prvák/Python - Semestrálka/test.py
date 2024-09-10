import pytest
from math import pi
from main import *

# Test cases for the function je_kladne()


def test_je_kladne_true():
    assert je_kladne(1, 2, 3)

def test_je_kladne_false():
    assert not je_kladne(-1, 2, 3)
    assert not je_kladne(1, -2, 3)
    assert not je_kladne(1, 2, -3)

# Test cases for the function obvod_obdelniku()

def test_obvod_obdelniku():
    assert obvod_obdelniku(2, 3) == 10

def test_obvod_obdelniku_negative_input():
    with pytest.raises(ValueError):
        obvod_obdelniku(-2, 3)
        obvod_obdelniku(2, -3)

# Test cases for the function obsah_obdelniku()

def test_obsah_obdelniku():
    assert obsah_obdelniku(2, 3) == 6

def test_obsah_obdelniku_negative_input():
    with pytest.raises(ValueError):
        obsah_obdelniku(-2, 3)
        obsah_obdelniku(2, -3)

# Test cases for the function obvod_ctverce()

def test_obvod_ctverce():
    assert obvod_ctverce(4) == 16

def test_obvod_ctverce_negative_input():
    with pytest.raises(ValueError):
        obvod_ctverce(-4)

# Test cases for the function obsah_ctverce()

def test_obsah_ctverce():
    assert obsah_ctverce(4) == 16

def test_obsah_ctverce_negative_input():
    with pytest.raises(ValueError):
        obsah_ctverce(-4)

# Test cases for the function obvod_kruhu()

def test_obvod_kruhu():
    assert obvod_kruhu(5) == 2 * pi * 5

def test_obvod_kruhu_negative_input():
    with pytest.raises(ValueError):
        obvod_kruhu(-5)

# Test cases for the function obsah_kruhu()

def test_obsah_kruhu():
    assert obsah_kruhu(5) == pi * 5 * 5

def test_obsah_kruhu_negative_input():
    with pytest.raises(ValueError):
        obsah_kruhu(-5)

# Test cases for the function obvod_trojuhelniku()

def test_obvod_trojuhelniku():
    assert obvod_trojuhelniku(3, 4, 5) == 12

def test_obvod_trojuhelniku_invalid_triangle():
    with pytest.raises(ValueError):
        obvod_trojuhelniku(1, 2, 10)
        

# Test cases for the function obsah_trojuhelniku()

def test_obsah_trojuhelniku():
    assert obsah_trojuhelniku(4, 3) == 6

def test_obsah_trojuhelniku_invalid_input():
    with pytest.raises(ValueError):
        obsah_trojuhelniku(-4, 3)

# Test cases for the function obvod_lichobezniku()

def test_obvod_lichobezniku():
    assert obvod_lichobezniku(3, 4, 5, 6) == 18

def test_obvod_lichobezniku_invalid_input():
    with pytest.raises(ValueError):
        obvod_lichobezniku(-3, 4, 5, 6)

# Test cases for the function obsah_lichobezniku()

def test_obsah_lichobezniku():
    assert obsah_lichobezniku(3, 4, 5) == 17.5

def test_obsah_lichobezniku_invalid_input():
    with pytest.raises(ValueError):
        obsah_lichobezniku(-3, 4, 5)

def test_obvod_obdelniku_negative_sides():
    with pytest.raises(ValueError):
        obvod_obdelniku(-2, -3)

def test_obsah_obdelniku_negative_sides():
    with pytest.raises(ValueError):
        obsah_obdelniku(-2, -3)

# Test pro obdélník s nulovými hodnotami

def test_obvod_obdelniku_zero_sides():
    with pytest.raises(ValueError):
        obvod_obdelniku(0, 3)

def test_obsah_obdelniku_zero_sides():
    with pytest.raises(ValueError):
        obsah_obdelniku(0, 3)

# Další testy pro čtverec


def test_obvod_ctverce_negative_side():
    with pytest.raises(ValueError):
        obvod_ctverce(-3)

def test_obsah_ctverce_negative_side():
    with pytest.raises(ValueError):
        obsah_ctverce(-3)

# Další testy pro kruh


def test_obvod_kruhu_negative_radius():
    with pytest.raises(ValueError):
        obvod_kruhu(-5)

def test_obsah_kruhu_negative_radius():
    with pytest.raises(ValueError):
        obsah_kruhu(-5)

# Další testy pro trojúhelník

def test_obvod_trojuhelniku_negative_sides():
    with pytest.raises(ValueError):
        obvod_trojuhelniku(-3, 4, 5)


def test_obsah_lichobezniku_negative_side():
    with pytest.raises(ValueError):
        obsah_lichobezniku(-3, 4, 5)
