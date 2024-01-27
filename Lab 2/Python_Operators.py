#Example 1 - Arithmetic operators
'''+	Addition	x + y	
-	Subtraction	    x - y	
*	Multiplication	x * y	
/	Division	    x / y	
%	Modulus	        x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y
'''
print(5 + 15)
print(5 - 15)
print(5 * 15)
print(5 / 15)
print(5 % 15)
print(2 ** 4)
print(5 // 15, "\n")

#Example 2 - Assignment operators
a = 5
print(a)
a += 5
print(a)
a -= 5
print(a)
a %= 2
print(a)
a = 5
a //= 2
print(a, "\n")

#Example 3 - Comparison Operators
print(1 > 0,
2 < 3,
1 == 1,
1 != 2, "\n")

#Example 4 - Logical Operators
print(1 > 0 and 2 < 4)
print(1 > 0 or 2 > 4)
print(not(1 > 2), "\n")

#Example 5 - Identity Operators
x, y = 5, 4
print(x is y, x is not y)