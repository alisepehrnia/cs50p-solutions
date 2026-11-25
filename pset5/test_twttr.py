from twttr import shorten

def test_1():
    assert shorten("HelLo") == "HlL"
    assert shorten("aPpLEe") == "PpL"