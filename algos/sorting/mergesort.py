numbers = list(map(int, input().split()))


def mergesort(a):
	if len(a)==1:
		return a
	else:
		mid = int(len(a)/2)
		return merge(a[0:mid], a[mid:len(a)])

def merge(a,b):
	a = mergesort(a)
	b = mergesort(b)
	i=0
	j=0

	merged = []
	while i< len(a) and j < len(b):
		if a[i] < b[j]:
			merged.append(a[i])
			i+=1
		else:
			merged.append(b[j])
			j+=1

	while i < len(a):
		merged.append(a[i])
		i+=1


	while j < len(b):
		merged.append(b[j])
		j+=1
	return merged
	
x = mergesort(numbers)
print (*x )