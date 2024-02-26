import re
from testfunc import matchtest

pattern = r"a.*b$"

matchtest(pattern, 'a', 'test 1')
matchtest(pattern, 'ab', 'test 2')
matchtest(pattern, 'a123xc', 'test 3')
matchtest(pattern, 'a21asdb', 'test 4')
