import re

def lowercase(match_object):
    return '_' + match_object.group('x').lower()
def camelToSnake(string):
    pattern = r"(?P<x>[A-Z]{1})"
    print(re.sub(pattern, lowercase, string))
    #marioBrothers
    #mario_brothers

camelToSnake("marioBrothers")
camelToSnake("thisIsCamelString")
camelToSnake("toBeOrNotToBe")