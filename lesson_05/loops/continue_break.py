# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for number in numbers:
#     if number == 5:
#         print("Stopping the loop at 5.")
#         break  # שובר את הלולאה כשמגיעים ל-5
#     if number == 3:
#         print("Number is 3 - going to the start...")
#         continue  # דולג על 3 ולא מדפיס אותו
#     if number % 2 == 0:
#         print(f"Even number: {number}")



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number == 5:
        print("Stopping the loop at 5.")
        break  # שובר את הלולאה כשמגיעים ל-5
    if number == 3:
        print("Number is 3 - going to the start...")
        continue  # דולג על 3 ולא מדפיס אותו

    print(f"{number = }")
