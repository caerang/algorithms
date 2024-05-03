# TODO 다시 구현(오류 있음)
n, k = map(int, input().split())

minus_one = n % k

result = 0
n = n - minus_one
while True:
    n = n // k
    result += 1
    if n == 1:
        break

result += minus_one
print(result)
