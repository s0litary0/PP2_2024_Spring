import re
from testfunc import matchtest

pattern = "[a-z]+_+[a-z]+"

matchtest(pattern, 'abcz', 'test 1')
matchtest(pattern, 'ab_', 'test 2')
matchtest(pattern, 'ab_zx', 'test 3')
matchtest(pattern, 'ab____xzc', 'test 4')
