import math

class Circle:
    def __init__(self, radius: float):
        self.__radius = radius

    @property
    def radius(self) -> float:
        return self.__radius

    @radius.setter
    def radius(self, value: float):
        if value <= 0:
            raise ValueError("Radius must be positive.")
        self.__radius = value

    @property
    def area(self) -> float:
        """החזרת שטח העיגול."""
        return math.pi * (self.__radius ** 2)

# שימוש במחלקה
circle = Circle(5)  # יצירת עיגול עם רדיוס 5

# קריאה לרדיוס דרך הגטר
print("Radius:", circle.radius)  # פלט: Radius: 5

# קריאה לשטח דרך הגטר
print("Area:", circle.area)  # פלט: Area: 78.53981633974483

# עדכון הרדיוס דרך הסטר
circle.radius = 10  # שינוי הרדיוס ל-10

# קריאה מחדש לרדיוס ולשטח
print("Updated Radius:", circle.radius)  # פלט: Updated Radius: 10
print("Updated Area:", circle.area)  # פלט: Updated Area: 314.1592653589793

# ניסיון לעדכן לרדיוס שלילי
try:
    circle.radius = -3  # יגרום ל-ValueError
except ValueError as e:
    print("Error:", e)  # פלט: Error: Radius must be positive.
