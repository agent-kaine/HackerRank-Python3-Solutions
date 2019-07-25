n=int(input())
i=1
for i in range(1, n):
	print(' ' * (n-i-1), '#' * i)
	i += 1
print('#' * n)