import numpy as np
def generate_vector(z1, z2, n):
	eq = np.array([1])
	prev = np.copy(eq)
	for i in range(1, n+1):
		degree = np.multiply( prev, z1 ) 
		if i > 1:
			degree = np.append(degree, [degree[1]])
			degree[1] = z2**i
		else:
			degree = np.append(degree, [z2**i])
		prev = np.copy(degree)
		eq = np.append(eq, degree)
	return eq


print(generate_vector(2,3,4))
		
	