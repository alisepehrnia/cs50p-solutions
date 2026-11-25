from bank import value

def test_hello_strings():
    assert value("hELLO") == 0
    assert value("Hello, you!") == 0
    assert value("HELLO") == 0
    assert value("HELLO TO you!") == 0

def test_h_strings():
    assert value("hELL") == 20
    assert value("h") == 20
    assert value("H") == 20
    assert value("HELL TO you!") == 20

def test_other_string():
    assert value("o") == 100
    assert value("Poll") == 100
    assert value("APplE") == 100