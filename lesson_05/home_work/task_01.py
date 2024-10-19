# איסוף הגיל מהמשתמש
age = int(input("Enter your age: "))

# איסוף השאלה האם יש למשתמש כרטיס כניסה
has_ticket = input("Do you have a ticket? (yes/no): ").lower() == 'yes'

# איסוף השאלה האם יש למשתמש אישור מיוחד
has_permission = input("Do you have special permission? (yes/no): ").lower() == 'yes'

# בדיקה אם המשתמש מעל גיל 18 ויש לו כרטיס
if age >= 18 and has_ticket:
    print("You can enter the club.")
# בדיקה אם המשתמש מעל גיל 18 ואין לו כרטיס
elif age >= 18 and not has_ticket:
    print("You cannot enter the club without a ticket.")
# בדיקה אם המשתמש מתחת לגיל 18 ויש לו אישור מיוחד
elif age < 18 and has_permission:
    print("You can enter the club with special permission.")
# אם אף אחד מהתנאים לא מתקיים
else:
    print("You cannot enter the club.")
