import re
from testfunc import matchtest

pattern = "[A-Z]{1}[a-z]+"

matchtest(pattern, 'abc', 'test 1')
matchtest(pattern, 'Abc', 'test 2')

