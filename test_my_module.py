import my_module

def test_add():
    assert my_module.add(2, 2) == 4
    assert my_module.add(0, 0) == 0
    assert my_module.add(-1, 1) == 0
    assert my_module.add(-1, -1) == -2

def test_subtract():
    assert my_module.subtract(5, 2) == 3
    assert my_module.subtract(5, 5) == 0
    assert my_module.subtract(-5, 2) == -7
    assert my_module.subtract(-5, -5) == 0

def test_multiply():
    assert my_module.multiply(2, 2) == 4
    assert my_module.multiply(0, 0) == 0
    assert my_module.multiply(-1, 1) == -1
    assert my_module.multiply(-1, -1) == 1

def test_divide():
    assert my_module.divide(4, 2) == 2
    assert my_module.divide(0, 1) == 0
    assert my_module.divide(-4, 2) == -2
    assert my_module.divide(4, -2) == -2
    assert my_module.divide(-4, -2) == 2
    try:
        my_module.divide(4, 0)
        assert False, "Expected ZeroDivisionError"
    except ZeroDivisionError:
        pass

