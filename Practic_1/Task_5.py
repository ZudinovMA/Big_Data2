n = int(input())

items = []
for i in range(1, n + 1):
    items += [i] * i

ans = map(str, items[:n])

print(' '.join(ans))
