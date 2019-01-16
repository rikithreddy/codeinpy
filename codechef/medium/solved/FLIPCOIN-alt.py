n,q = map(int,input().split())
start ={}
end = {}
for _ in range(q):
	x,a,b = map(int,input().split())

	if x ==0:
		try:
			start[a]=start[a]+1
		except:
			start[a]=1

		try:
			end[b] +=1
		except:
			end[b]=1

	if x==1:
		count = 0
		heads = 0
		for i in range(a,b+1):
			try:
				count+=start[i]
			except:
				skip = 1
			try:
				count-=end[i]
			except:
				skip =1
			if count%2==1:
				heads+=1				


		print(heads)
