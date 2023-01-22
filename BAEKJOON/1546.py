n = int(input())
score = list(map(int,input().split()))
result = []
for i in range(len(score)) : 
    result.append(score[i]/max(score)*100)
print(sum(result)/len(result))