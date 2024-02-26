import re
from testfunc import subtest

pattern = "[ ,.]"

subtest(pattern, 'ab  cz', ':', 'test 1')
subtest(pattern, 'ab.,', ':', 'test 2')
subtest(pattern, 'ab ,.zx', ':','test 3')
subtest(pattern, 'ab.xzc', ':','test 4')
