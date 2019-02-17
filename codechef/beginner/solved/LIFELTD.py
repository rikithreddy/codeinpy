# cook your dish here
import sys
for _ in range( int(sys.stdin.readline())):
	l =[]
	l.append( list( sys.stdin.readline().strip()  )) 
	l.append( list( sys.stdin.readline().strip()  )) 
	l.append( list( sys.stdin.readline().strip()  )) 
	x = False
	for i in range(2):
		for j in range(2):
			if l[i][j] == l[i+1][j] and l[i+1][j+1] == l[i+1][j] and l[i][j] == 'l':
				x = True

	sys.stdout.write( 'yes\n' if x else  'no\n' )
