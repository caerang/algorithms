n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[-1]
second = data[-2]

result = ((k * first)+second) * (m // (k+1)) + (m % (k+1)) * first

print(result)