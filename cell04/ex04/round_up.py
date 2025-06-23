#!/urs/bin/python3

import math

try:
    number_str = input("Give me a number: ")
    input_number = float(number_str)

    rounded_up_number = math.ceil(input_number)
    print(f"The number rounded up is: {rounded_up_number}")

except ValueError:
    print("Invalid input. Please give a valid number.")

