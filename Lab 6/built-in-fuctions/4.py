from time import sleep
from math import sqrt

def sqrt_after_milliseconds(num, time_ms):
    sleep(time_ms / (10 ** 3))
    print(f"Square root of {num} after {time_ms} miliseconds is {sqrt(num)}")

sqrt_after_milliseconds(int(input()), int(input()))