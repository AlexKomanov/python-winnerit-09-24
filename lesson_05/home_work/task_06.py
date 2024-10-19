def calculate_average(nums_array):
    if not nums_array:  # בדיקה אם הרשימה ריקה
        return 0

    total = 0  # משתנה לאחסון הסכום
    count = 0  # משתנה לאחסון מספר האיברים
    for num in nums_array:
        total += num  # חיבור כל איבר לסכום
        count += 1  # ספירת האיברים

    return total / count  # חישוב ממוצע



numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print(average)
