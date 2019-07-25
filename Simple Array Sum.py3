def simpleArraySum(ar):
	sum = 0
	for i in ar:
		sum += i
	return sum

ar_count = int(input())
ar = list(map(int, input().rstrip().split()))
print(simpleArraySum(ar))