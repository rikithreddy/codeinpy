import sys

def exp_print(n):
	i=15
	str_ =""
	while(i>-1):		
		x = pow(2,i)

		if n&x >0:
			if i==1:
				if(n&i ==1):
					str_+='2+'
				else:
					str_+='2'
			elif i==0:
				str_+='2(0)'
			else:
				str_+='2(%s)+' % exp_print(i)
		i-=1
	return str_


sys.stdout.write(exp_print(137)+'\n')
sys.stdout.write(exp_print(1315)+'\n')
sys.stdout.write(exp_print(73)+'\n')
sys.stdout.write(exp_print(136)+'\n')
sys.stdout.write(exp_print(255)+'\n')
sys.stdout.write(exp_print(1384)+'\n')
sys.stdout.write(exp_print(16385)+'\n')