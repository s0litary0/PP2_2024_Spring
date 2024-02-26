import re

def snake_toUpper(text):
    a = re.split('_{1}', text)
    print(a[0] + ''.join(map(lambda x: x.title(), a)))

snake_toUpper('snake_string')
snake_toUpper('winter_summer_holidays')
snake_toUpper('fruits_apple')
snake_toUpper('red_blue_yellow_green')