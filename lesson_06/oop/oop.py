class Dog:
    def __init__(self, name, age):
        self.name = name  # תכונה
        self.age = age  # תכונה

    def bark(self):
        print("Woof!")  # מתודה שמדפיסה נביחה

    def get_info(self):
        return f"{self.name} is {self.age} years old."  # מתודה שמחזירה מידע על הכלב

    def get_age(self):
        return self.age


dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# שימוש במתודות
print(dog1.get_info())  # פלט: Buddy is 3 years old.
dog2.bark()# פלט: Woof!
print(dog1.age)
