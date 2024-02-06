# test_string_converter.py

from string_converter import make_upper, make_capital, make_lower

def test_make_upper():
    assert make_upper("hello") == "HELLO"
    assert make_upper("Python") == "PYTHON"
    assert make_upper("Test123") == "TEST123"

def test_make_capital():
    assert make_capital("hello") == "Hello"
    assert make_capital("python") == "Python"
    assert make_capital("test123") == "Test123"

def test_make_lower():
    assert make_lower("HELLO") == "hello"
    assert make_lower("Python") == "python"
    assert make_lower("Test123") == "test123"

def test_script():
    test_make_upper()
    test_make_capital()
    test_make_lower()

# Run the tests using the following command:

