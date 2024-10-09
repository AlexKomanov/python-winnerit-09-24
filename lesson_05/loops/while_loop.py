# count = 0
#
# while count < 5:
#     print(count)
#     count += 1

num = int(input("Guess a number: "))
num_of_attempts = 3
num_of_attempts -= 1

while num != 5 and num_of_attempts > 0:
    print(f"{num_of_attempts}")
    print(f"Wrong Number: {num}. Try Again")
    num = int(input("Guess a number: "))
    num_of_attempts -= 1

if num_of_attempts > 0:
    print("You Guessed a Number!")
else:
    print("Yuo lose")