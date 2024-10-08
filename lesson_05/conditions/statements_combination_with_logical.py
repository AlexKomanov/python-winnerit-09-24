experience = int(input("Enter your experience: "))
language = input("Enter your language: ")

if experience >= 3 and language == "Python":
    print("You're matching a job!")
elif experience >= 2 and language == "Java":
    print("You're matching a job!")
elif experience >= 5 and language == "JavaScript":
    print("You're matching a job!")
else:
    print("You need to improve your skills!")