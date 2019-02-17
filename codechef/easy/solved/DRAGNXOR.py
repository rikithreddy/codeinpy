import sys

def num_ones(n):
	count = 0
	while( n != 0 ):
		count += 1
		n &= (n-1)

	return count
for _ in range(int(sys.stdin.readline())):
	n, a, b = map(int, sys.stdin.readline().split())
	a1 = bin(a)[2:]
	b1 = bin(b)[2:]
	a_ = num_ones(a)
	b_ = num_ones(b)

	l = pow(2,n)-1
	if a_ + b_ > n:
		t = a_ + b_ - n 
		d = pow(2,t)-1
		sys.stdout.write( str(l^d) +'\n' )

	elif a_ + b_ == n:
		sys.stdout.write( str(l) +'\n' )

	else:

		t = n - (a_ + b_)
		d = pow(2,t)-1
		sys.stdout.write( str(l^d) +'\n' )

