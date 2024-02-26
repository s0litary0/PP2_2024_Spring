import re

def matchtest(pattern, testData, testNumber):
    if re.search(pattern, testData) != None:
        print(testNumber + " is passed!")
    else: 
        print(testNumber + " is not passed!")

def subtest(pattern, text, replaceWith, testNumber):
    print(re.sub(pattern, replaceWith, text))
    
