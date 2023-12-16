import decimal
import time
import datetime

def compute_pi(precision):
    decimal.getcontext().prec = precision + 2
    pi = decimal.Decimal(0)
    for k in range(precision):
        pi += (decimal.Decimal(1)/(16**k))*(
            (decimal.Decimal(4)/(8*k+1)) -
            (decimal.Decimal(2)/(8*k+4)) -
            (decimal.Decimal(1)/(8*k+5)) -
            (decimal.Decimal(1)/(8*k+6))
        )
    return pi

digits = input("Enter the number of digits of pi to calculate: ")
precision = int(digits)

pi = compute_pi(precision)

pi_str = str(pi)

color_red = "\033[91m"
color_green = "\033[92m"
color_reset = "\033[0m"

typing_delay = 0.001  
for char in pi_str:
    if char.isdigit():
        print(color_green + char + color_reset, end='', flush=True)
    else:
        print(color_red + char + color_reset, end='', flush=True)
    time.sleep(typing_delay)

current_datetime = datetime.datetime.now()
filename = f"pi_digits_{current_datetime.strftime('%Y%m%d_%H%M%S')}.txt"

with open(filename, "w") as file:
    file.write(pi_str)

highest_pi_filename = "highestpi.txt"
try:
    with open(highest_pi_filename, "r") as file:
        highest_pi = file.read()
    if len(pi_str) > len(highest_pi):
        with open(highest_pi_filename, "w") as file:
            file.write(pi_str)
except FileNotFoundError:
    with open(highest_pi_filename, "w") as file:
        file.write(pi_str)
    
print(f"\nDigits of pi have been saved to '{filename}'.")
print(f"Highest value of pi is saved in '{highest_pi_filename}'.")
