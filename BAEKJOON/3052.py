## (1) 1차 작성
# import sys
# N = [int(sys.stdin.readline())%42 for i in range(10)]
# sum = {}

# for i in N:
#     try: sum[i] += 1
#     except: sum[i] = 1
# print(len(sum))

## (2) 수정
n = []
for _ in range(10):
    a = int(input())
    n.append(a%42)
n = set(n)
print(len(n))