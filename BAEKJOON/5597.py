idx = [i for i in range(1,31)]

for _ in range(28) :
    n = int(input())
    idx.remove(n)

print(min(idx))
print(max(idx))
