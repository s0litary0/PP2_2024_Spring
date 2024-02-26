import re

def splitTest(text):
    print(re.findall('[A-Z]{1}[a-z]*', text))

splitTest('TodayIsAGoodDay')
splitTest('WashThePoisonFromOfMySkin')