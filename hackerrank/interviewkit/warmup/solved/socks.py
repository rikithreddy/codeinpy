import sys
from collections import Counter
int(sys.stdin.readline())
x = Counter(list(map(int, sys.stdin.readline().split())))
sys.stdout.write(  str(sum(  [p//2 for p in x.values()]  ) )    )