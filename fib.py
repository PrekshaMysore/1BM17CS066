Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=0
>>> b=1
>>> fib=[a,b]
>>> while b<70:
	a,b=b,a+b
	fib.append(b)

	
>>> print(fib)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> a=0
>>> b=1
>>> n=int(input("enter a number"))
enter a number5
>>> fib=[a,b]
>>> while b<n:
	a,b=b,a+b
	fib.append(b)

	
>>> print (fib)
[0, 1, 1, 2, 3, 5]
>>> 
