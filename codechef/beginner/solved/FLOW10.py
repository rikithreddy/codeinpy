t = int(input())


for i in range(t):
	x = input().strip()

	if x in ['b','B']:
		print('BattleShip')
	if x in ['c','C']:
		print('Cruiser')
	if x in ['d','D']:
		print('Destroyer')
	if x in ['f','F']:
		print('Frigate')

