h, m = map(int, input().split())
t = int(input())

h = h % 24

if (m+t) >= 60:
    h = h+((m+t)//60)
    m = (m+t) % 60
    if h >= 24:
        h = (h % 24)
else:
    m = m+t

print(h, m)
