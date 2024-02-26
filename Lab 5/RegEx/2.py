import re
from testfunc import matchtest

pattern = "ab{2,3}"

matchtest(pattern, 'a', 'test 1')
matchtest(pattern, 'ab', 'test 2')
matchtest(pattern, 'abbb', 'test 3')
matchtest(pattern, 'abbbb', 'test 4')

