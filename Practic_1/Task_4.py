ans = [0, 0]
while True:
    i = int(input())
    ans[0] += i
    ans[1] += i**2
    if not ans[0]:
        break
print(ans[1])
