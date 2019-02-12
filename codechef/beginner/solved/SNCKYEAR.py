from sys import stdin, stdout
for _ in range( int(stdin.readline()) ):
	if int(stdin.readline()) in [2010, 2015, 2016, 2017, 2019]:
		stdout.write('HOSTED\n')
	else:
		stdout.write('NOT HOSTED\n')
