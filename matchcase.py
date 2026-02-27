def is_weekend(day):
    match day:
        case "Sunday":
            return True
        case "Monday":
            return False
        case "Tuesday":
            return False
        case "Wednessday":
            return False
        case "Thursday":
            return False
        case "Friday":
            return False
        case "Saturday":
            return True
        case _:
            return False


print(is_weekend("Sunday"))
