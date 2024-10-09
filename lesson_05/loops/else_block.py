# # הגדרת מערך של מספרים
# numbers = [1, 2, 3, 4, 5]
# search_number = 2  # המספר שאנחנו מחפשים
#
# # חיפוש המספר במערך
# for number in numbers:
#     if number == search_number:
#         print(f"Found {search_number} in the list!")
#         break
# else:
#     print(f"{search_number} not found in the list.")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number == 8:
        break
    print(number, end=" ")
else:
    print("\nAll iterations were finished")