MAX = 4000000

def e0002_000():
	return 4613732

def e0002_001():
	a, b, s = 1, 1, 0
	while b < MAX: 
		a, b = b, b + a
		if not b % 2: s += b
	
	return s

def e0002_002():
	a, b, s = 1, 2, 0
	while s < MAX:
		s += b
		a, b = 2 * b + a, 3 * b + 2 * a
	return s

def e0002_003():
	a, b, s = 1, 2, 0
	while s < MAX:
		s += b
		a, b = b+b + a, b+b+b + a+a
	return s

# sum even to fib(n) = (fib(n + 2) - 1) / 2
def e0002_004():
	a, b = 1, 2
	while b < MAX:
		a, b = b+b + a, b+b+b + a+a
	return (a-1)//2

def e0002_005():
	a, b, c, s = 2, 3, 5, 0
	while a < MAX: 
		s += a
		a = b + c
		b = c + a
		c = b + a
	return s

def e0002_006():
	a, b, c = 2, 3, 5
	while c < MAX: 
		a = b + c
		b = c + a
		c = b + a
	return (c - 1) // 2

def e0002_007():
	a, b =  0, 2
	while b < MAX:
		a, b = b, a + 4*b
	return (b+a-2)//4

from math import log
def e0002_008():
	sq = 5 ** .5
	n = log(MAX * sq)//log(2 + sq)
	x = (2 + sq)
	y = (2 - sq)
	return int(((x-x**(n+1)) / (1-x) - (y-y**(n+1)) / (1-y))/sq)
# Better for HUGE MAX

if __name__ == '__main__':
	from __init__ import start
	start(e0002_000())