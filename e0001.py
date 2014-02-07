
def e0001_000():
	return 233168

def e0001_001():
	total = 0
	for x in range(1000):
		if x % 3 == 0 or x % 5 == 0:
			total += x
	return total

def e0001_002():
	total = 0
	for x in xrange(1000):
		if x % 3 == 0 or x % 5 == 0:
			total += x
	return total

def e0001_003():
	return sum(i for i in range(3, 1000) if i % 3 == 0 or i % 5 == 0)

def e0001_004():
	return sum(i for i in xrange(3, 1000) if i % 3 == 0 or i % 5 == 0)

def e0001_005():
	return sum(set(range(3,1000,3)) | set(range(5,1000,5)))

def e0001_006():
	return sum(set(xrange(3,1000,3)) | set(xrange(5,1000,5)))

def e0001_007():
	return sum(range(5,1000,5)) + sum(range(3,1000,3)) - sum(range(15,1000,15))

def e0001_008():
	return sum(xrange(5,1000,5)) + sum(xrange(3,1000,3)) - sum(xrange(15,1000,15))

def e0001_009():
	def sumx(n,x):
		n = (n - 1)/x
		return x * n/2. * (n + 1)
	
	return sumx(1000,5) + sumx(1000,3) - sumx(1000,15)

def e0001_010():
	def sumx(n,x):
		n = (n - 1)//x
		return x * n/2. * (n + 1)
	
	return sumx(1000,5) + sumx(1000,3) - sumx(1000,15)

def e0001_011():
	def sumx(n,x):
		n = (n - 1)//x
		return x * n * (n + 1) / 2
	
	return sumx(1000,5) + sumx(1000,3) - sumx(1000,15)

def e0001_012():
	def sumx(n,x):
		n = (n - 1)//x
		return x * n * (n + 1) // 2
		
	return sumx(1000,5) + sumx(1000,3) - sumx(1000,15)


if __name__ == '__main__':
	from __init__ import start
	start(e0001_000())