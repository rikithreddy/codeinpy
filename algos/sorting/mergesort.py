numbers = map(int, input().split())

def mergesort(a):
	if len==1:
		return a
	else:
		return merge(a[0:int(len(a)/2)], a[int(len(a)/2):len(a)])

def merge(a,b):
	a = mergesort(a)
	b = mergesort(b)

	for
