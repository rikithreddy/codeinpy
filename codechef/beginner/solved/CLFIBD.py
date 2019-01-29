for t in range(int(input())):
    S = input().lower()
    dist = []
    counts = []
    for j in S:
      if j not in dist:
        dist.append(j)
        counts.append(S.count(j))
    if(len(dist)<3):
      print("Dynamic")
      continue
    flag = 0
    counts.sort()
    l = len(counts)
    if(counts[l-1] == (counts[l-2]+counts[l-3])):
        print("Dynamic")
    else:
        print("Not")