text = input("Enter a first word: ")
text_2 = input("Enter a second word: ")

print(text_2[::-1])

if text.lower() == text_2[::-1].lower():
    print('YES')
else:
    print('NO')