from myapp.app import add, subtract

def test_add():
    """Перевірка функції додавання"""
    assert add(2, 3) == 5

def test_subtract():
    """Перевірка функції віднімання"""
    assert subtract(5, 3) == 2