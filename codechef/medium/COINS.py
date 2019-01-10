


def max_val(num):
	if num == 0 or num == 1:
		return num
	if num in dp:
		return dp[num]
	maxval = max(num,max_val(num//2)+max_val(num//3)+max_val(num//4))
	dp[num] = maxval
	return maxval

if __name__=='__main__':
	global dp
	dp = {}

	for i in range(10):

		try:
			n = int(input())
			print(max_val(n))
		except:
			break
