n,k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
minimum_score = arr[k-1]
count = 0
for i in arr:
    if i<minimum_score or i==0:
        break
    else:
        count+=1
print(count)