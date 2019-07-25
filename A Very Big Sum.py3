ar_count = int(input())
ar = list(map(int, input().rstrip().split()))
sum = 0
for i in ar:
	sum += i
print(sum)