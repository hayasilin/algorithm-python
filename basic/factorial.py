# Recursion

def factorial(i):
	if i == 0:
		return 1
	else:
		result = i * factorial(i - 1)

	return result

print(factorial(10))

def fib(n):
	if n == 0:
		return 0
	elif n == 1 or n == 2:
		return 1
	else:
		return (fib(n-1) + fib(n-2))

n = int(input('please input a number'))
for i in range(n + 1):
	print('fib(%d) = %d' %(i, fib(i)))

# Dynamic programming

output = [None]*1000

def fibonacci(n):
	result = output[n]

	if result == None:
		if n == 0:
			result = 0
		elif n == 1:
			result = 1
		else:
			result = fibonacci(n-1) + fibonacci(n-2)

		output[n] = result

	return result

print(fibonacci(10))