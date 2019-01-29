global values
values=[1]
i = 2
while values[i-2]<=1000000000:
	values.append(values[i-2]+i)
	i+=1
values.append(values[i-2]+i)
t = int(input())


def get_index(x,start,end):
	if (start <= end):
		mid = (start+end)//2

		if values[mid] == x:
			return mid 
		if values[mid] > x:
			return get_index(x,start,mid-1)
		elif values[mid] < x:
			return get_index(x,mid+1,end)
	else:
		return end

for i in range(t):
	x = int(input())
	l = len(values)
	L=(get_index(x,0,l-1))	

	print(min(L+x-values[L],L+1+values[L+1]-x)+1)