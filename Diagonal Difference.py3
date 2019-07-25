n = int(input().strip())
arr = []
for _ in range(n):
	arr.append(list(map(int, input().rstrip().split())))
s1 = 0; s2 = 0;
for i in range(l):
	s1 += arr[i][i]
	s2 += arr[i][n-i-1]
print(abs(s1 - s2))