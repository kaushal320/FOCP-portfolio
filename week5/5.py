#Last week you wrote a program that processed a collection of temperature readings
#entered by the user and displayed the maximum, minimum, and mean. Create a
#version of that program that takes the values from the command-line instead. Be
#sure to handle the case where no arguments are provided! 

import sys

def convert_to_fah(celsius):
    fahren = float(celsius * 9 / 5) + 32
    return fahren

if len(sys.argv) < 2:
    print("No temperature values provided.")
else:
    celsius = [round(float(temp[:-1]), 2) for temp in sys.argv[1:]]

    fahrenheit = [convert_to_fah(temp) for temp in celsius]

    max_temp = max(fahrenheit)
    min_temp = min(fahrenheit)
    mean_temp = sum(fahrenheit) / len(fahrenheit)

    print(f"Maximum temperature: {max_temp:.2f}F")
    print(f"Minimum temperature: {min_temp:.2f}F")
    print(f"Mean temperature: {mean_temp:.2f}F")