from fuel import convert, gauge
import pytest

def test_convert():
    with pytest.raises(ValueError): convert("jj4k5")
    with pytest.raises(ValueError): convert("Ki4/3")
    with pytest.raises(ValueError): convert("3/0")
    assert convert("1/4") == 25
    assert convert("1/6") == 17
    assert convert("1/10") == 10
    assert convert("1/1000") == 0
    assert convert("999/1000") == 100

def test_gauge():
    assert gauge(99.1) == "F"
    assert gauge (0.99) == "E"
    assert gauge(25.34) == "25.34%"
    assert gauge(33.333) == "33.333%"