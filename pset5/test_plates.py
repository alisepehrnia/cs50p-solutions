from plates import is_valid

def test_length():
    assert(is_valid("AA")) == True
    assert(is_valid("aP1254")) == True
    assert(is_valid("aP1254o")) == False
    assert(is_valid("aP12540")) == False

def test_two_letters_start():
    assert(is_valid("a0")) == False
    assert(is_valid("0a")) == False
    assert(is_valid("z29878")) == False
    assert(is_valid("229898")) == False
    assert(is_valid("pz")) == True

def test_first_num_not_zero():
    assert(is_valid("aa2")) == True
    assert(is_valid("aa5")) == True
    assert(is_valid("aa9")) == True
    assert(is_valid("aa0")) == False
    assert(is_valid("aa012")) == False

def test_number_comes_at_end():
    assert(is_valid("aa1245")) == True
    assert(is_valid("aapq45")) == True
    assert(is_valid("aap4qp5")) == False