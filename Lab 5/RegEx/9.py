import re

def test(pattern, text, testNumber):
    print(re.sub(pattern, r"\1 \2", text))

pattern = r'([a-zA-Z])([A-Z])'
test(pattern, "MySuperTest", "test1")
test(pattern, " MySuperTest IAmRobot", "test2")