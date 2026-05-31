def convert(numeral: str) -> int:
    match numeral.upper():
        case "I" | "i":
            return 1
        case "V" | "v":
            return 5
        case "X" | "x":
            return 10
        case "L" | "l":
            return 50
        case "C" | "c":
            return 100
        case "D" | "d":
            return 500
        case "M" | "m":
            return 1000
        case _ as invalid:
            raise ValueError(f"{invalid} is not a valid Roman numeral")


def parse(numerals: str) -> int:
    total = 0
    length = len(numerals)

    for i in range(length):
        current_value = convert(numerals[i])

        if i + 1 < length and current_value < convert(numerals[i + 1]):
            total -= current_value
        else:
            total += current_value

    return total
