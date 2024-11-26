# test_calculator.py
import pytest
from source.calculator import add

# בדיקה עם פרמטרים שונים
@pytest.mark.parametrize("x, y, expected", [
    (1, 2, 3),    # חיבור של שני מספרים חיוביים
    (-1, 1, 0),   # חיבור של מספר חיובי ושלילי
    (0, 0, 0),    # חיבור של שני אפסים
    (5, 5, 10),   # חיבור של שני מספרים זהים
    (-3, -3, -6)  # חיבור של שני מספרים שליליים
])
def test_add(x, y, expected):
    assert add(x, y) == expected
