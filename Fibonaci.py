import time

def Fibonaci_recursively(n):
	if n == 1:
		return 0
	if n == 2:
		return 1
	return Fibonaci_recursively(n-2) + Fibonaci_recursively(n-1)

def Fibonaci_iteratively(n):
	if n == 1:
		return 0
	if n == 2:
		return 1
	a = 0
	b = 1
	while n >2:
		a, b = b, a+b
		n -= 1
	return b

if __name__ == '__main__':
	start1 = time.clock()
	Fibonaci_recursively(5)
	print('Time used recursively: %s' % (time.clock() - start1))
	start2 = time.clock()
	Fibonaci_iteratively(5)
	print('Time used iteratively: %s' % (time.clock() - start2))
