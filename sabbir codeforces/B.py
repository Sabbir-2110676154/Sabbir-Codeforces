t = int(input())

for _ in range(t):
    a, b, m = map(int, input().split())

    tmp = 2
    tmp += (m // b)
    tmp += (m // a)

    print(tmp)