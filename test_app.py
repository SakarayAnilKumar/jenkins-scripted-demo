from app import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-5, -5) == -10

def test_add_with_floats():
    assert add(2.5, 3.5) == 6.0
    assert add(-1.5, 1.5) == 0.0
    assert add(0.0, 0.0) == 0.0
    assert add(-5.5, -4.5) == -10.0

def test_add_with_large_numbers():
    assert add(1_000_000, 2_000_000) == 3_000_000
    assert add(-1_000_000, -2_000_000) == -3_000_000
    assert add(1_000_000, -1_000_000) == 0
    assert add(999_999, 1) == 1_000_000

def test_add_with_zero():
    assert add(0, 5) == 5
    assert add(5, 0) == 5
    assert add(0, 0) == 0
    assert add(-5, 0) == -5

def test_add_with_negative_numbers():
    assert add(-2, -3) == -5
    assert add(-1, -1) == -2
    assert add(-5, 5) == 0
    assert add(-10, -20) == -30

def test_add_with_mixed_numbers():
    assert add(-2, 3) == 1
    assert add(2, -3) == -1
    assert add(-5, 5) == 0
    assert add(10, -20) == -10

def test_add_with_large_floats():
    assert add(1e10, 1e10) == 2e10
    assert add(-1e10, -1e10) == -2e10
    assert add(1e10, -1e10) == 0
    assert add(1.5e10, 2.5e10) == 4.0e10

def test_add_with_small_floats():
    assert add(1e-10, 1e-10) == 2e-10
    assert add(-1e-10, -1e-10) == -2e-10
    assert add(1e-10, -1e-10) == 0
    assert add(1.5e-10, 2.5e-10) == 4.0e-10

def test_add_with_large_and_small_numbers():
    assert add(1e10, 1e-10) == 1e10
    assert add(-1e10, -1e-10) == -1e10
    assert add(1e10, -1e-10) == 1e10
    assert add(-1e10, 1e-10) == -1e10

def test_add_with_large_and_small_floats():
    assert add(1e10, 1e-10) == 1e10
    assert add(-1e10, -1e-10) == -1e10
    assert add(1e10, -1e-10) == 1e10
    assert add(-1e10, 1e-10) == -1e10

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-1, -1) == 0
    assert subtract(0, 0) == 0
    assert subtract(-5, -5) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 5) == 0
    assert multiply(-5, -5) == 25

def test_divide():
    assert divide(6, 3) == 2
    assert divide(-6, 3) == -2
    assert divide(0, 5) == 0
    assert divide(-10, -2) == 5

def test_divide_by_zero():
    try:
        divide(5, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero."
    else:
        assert False, "Expected ValueError for division by zero"