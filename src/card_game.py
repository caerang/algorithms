i, j = map(int, input().split())

result = 0

for _ in range(i):
    data = list(map(int, input().split()))

    min_value = 10001
    for v in data:
        min_value = min(min_value, v)
    result = max(min_value, result)

print(result)
