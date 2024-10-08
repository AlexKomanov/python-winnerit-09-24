day = input("Enter a day of the week: ")

match day.lower():
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        if day.lower() == "friday":
            print("Today is Friday")
        print("Weekday")
    case "saturday" | "sunday":
        print("Weekend")
    case _:
        print("Invalid day")
