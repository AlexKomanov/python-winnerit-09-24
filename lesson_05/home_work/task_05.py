def find_max(*args):
    if not args:  # בדיקה אם לא הועברו ארגומנטים
        return "No numbers were given"

    max_num = args[0]  # מניחים שהמספר הראשון הוא המקסימלי
    for num in args:
        if num > max_num:  # אם מוצאים מספר גדול יותר
            max_num = num  # מעדכנים את המספר המקסימלי

    return max_num  # החזרת המספר המקסימלי


# דוגמה להרצה
max_number = find_max(3, 7, 2, 8, 10, 4)
print(max_number)  # פלט: 10

max_number = find_max()
print(max_number)  # פלט: No numbers were given