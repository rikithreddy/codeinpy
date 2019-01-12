t = int(input())



for i in range(t):
	feedback = input()
	if '010' in feedback or '101' in feedback:
		print('Good')
	else:
		print('Bad')