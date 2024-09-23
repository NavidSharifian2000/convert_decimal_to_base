import math

def number_to_char(number):
    if number == 10:
        return "A"
    elif number == 11:
        return "B"
    elif number == 12:
        return "C"
    elif number == 13:
        return "D"
    elif number == 14:
        return "E"
    elif number == 15:
        return "F"
    else:
        return str(number)

def convert_fractional_part(decimal_fraction, base):
    iteration_count = 0
    result = ""
    while iteration_count < 10:
        decimal_fraction *= base
        result += number_to_char(int(decimal_fraction))
        decimal_fraction, _ = math.modf(decimal_fraction)
        iteration_count += 1
    return result

def convert_integer_part(integer, base):
    result = ""
    while integer != 0:
        result += number_to_char(integer % base)
        integer //= base
    return result[::-1] + "/"

def convert_decimal_to_base(decimal_number, base):
    fractional_part, integer_part = math.modf(decimal_number)
    integer_part = int(integer_part)
    return convert_integer_part(integer_part, base) + convert_fractional_part(fractional_part, base)

print(convert_decimal_to_base(12, 8))
