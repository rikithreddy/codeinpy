from sys import stdin, stdout

for __ in range(int(stdin.readline())):
	 x = stdin.readline().strip()
	 last = "0"
	 c = 0 
	 for i in x:
	 	if last != i and i == '1':
	 		c+=1
	 		last = "1"
	 		if c == 2: break
	 	elif i =="0":
	 		last = "0"	
	 stdout.write("NO\n" if c != 1 else "YES\n")