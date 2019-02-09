import sys 
x = sys.stdin.readline().strip()
if x in ['a','e','i','u','o','A', 'E', 'I', 'O', 'U']:
	sys.stdout.write("Vowel\n")
else:
	sys.stdout.write("Consonant\n")
