def get_color_name(color_code):
    match color_code:
        case 1:
            return "Red"
        case 2:
            return "Green"
        case 3:
            return "Blue"
        case _:
            return "Unknown"

print(get_color_name(1))  # Output: Red
print(get_color_name(4))  # Output: Unknown

def check_value(value):
    match value:
        case "a" | "e" | "i" | "o" | "u":
            return "Vowel"
        case 0 | 2 | 4 | 6 | 8:
            return "Even Number"
        case _:
            return "Other"

print(check_value("e"))  # Output: Vowel
print(check_value(5))   # Output: Other
