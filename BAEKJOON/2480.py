a, b, c = map(int, input().split())

if (a == b and b == c and a == c):
    m = 10000+(a*1000)
elif (a == b or b == c or c == a):
    if (a == b):
        m = 1000+(a*100)
    elif (b == c):
        m = 1000+(b*100)
    else:
        m = 1000+(c*100)
else:
    if (a > b and a > c):
        m = a*100
    elif (b > c and b > a):
        m = b*100
    else:
        m = c*100
print(m)
