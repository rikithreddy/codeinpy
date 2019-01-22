t = int(input())

for _ in range(t):
	d, u, n = map(float,input().split())
	index = 0
	mini = d*u

	for i in range(int(n)):
		m, r, c = map(float,input().split())
		m_c = c/m
		r_u = u*r 
		if m_c+r_u <= mini:

			mini = m_c+r_u
			index = i+1

	print(index)			

