n = int(input())
arr = list(map(int, input().rstrip().split()))
ar = [0, 0, 0]
for i in arr:
	if i > 0:
		ar[0] += 1
	elif i < 0:
		ar[1] += 1
	else:
		ar[2] += 1
print(ar[0] / n)
print(ar[1] / n)
print(ar[2] / n)