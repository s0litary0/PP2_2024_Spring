import re
from testfunc import matchtest

pattern = ".*ab*"

matchtest(pattern, '', 'test 1')
matchtest(pattern, 'a', 'test 2')
matchtest(pattern, 'ab', 'test 3')
matchtest(pattern, 'abbbb', 'test 4')