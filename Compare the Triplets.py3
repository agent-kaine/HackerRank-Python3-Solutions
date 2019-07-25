a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
ar = [0, 0]
for i in range(3):
	if a[i] > b[i]:
		ar[0] += 1
	if b[i] > a[i]:
		ar[1] += 1
print(' '.join(map(str, ar)))