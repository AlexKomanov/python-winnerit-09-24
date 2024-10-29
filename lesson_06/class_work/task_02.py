# קלאס האב
class Person:
    def __init__(self, name):
        # תכונה מוגנת
        self._name = name

    # מתודה בקלאס האב שמחזירה את השם
    def get_name(self):
        return f"Name from Person class: {self._name}"


# קלאס הבן שיורש את קלאס האב
class Student(Person):
    def __init__(self, name, student_id):
        # קריאה לקונסטרקטור של קלאס האב
        super().__init__(name)
        # תכונה פרטית נוספת בקלאס הבן
        self.__student_id = student_id

    # מתודה בקלאס הבן שמחזירה את מספר הסטודנט
    def display_student_id(self):
        return f"Student ID: {self.__student_id}"

    # שימוש ב-property עבור גטר וסטר לשם מהקלאס האב
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

# יצירת אובייקטים ובדיקת הפלט
person = Person("Alice")
print(person.get_name())

student = Student("Alex", "S12345")
print(student.name)
print(student.display_student_id())

# עדכון השם דרך הסטר
student.name = "Bob"
print(student.name)

