# You have a positive integer m and a non-negative integer s. Your task is to find the smallest and the largest of the numbers that have length m and sum of digits s. The required numbers should be non-negative integers written in the decimal base without leading zeroes.

# Input
# The single line of the input contains a pair of integers m, s (1 ≤ m ≤ 100, 0 ≤ s ≤ 900) — the length and the sum of the digits of the required numbers.

# Output
# In the output print the pair of the required non-negative integer numbers — first the minimum possible number, then — the maximum possible number. If no numbers satisfying conditions required exist, print the pair of numbers "-1 -1" (without the quotes).

# Examples
# inputCopy
# 2 15
# outputCopy
# 69 96
# inputCopy
# 3 0
# outputCopy
# -1 -1
# found = 0
# def util(m,s,arr,res):
#     global found
#     if found==1:
#         return 
#     if len(arr)<=m and s>=0:
#         if len(arr)==m and s==0 and arr[0]!=0:
#             res.append(''.join([str(x) for x in arr]))
#             found = 1
#             return 
#         for i in range(9,-1,-1):
#             arr.append(i)
#             if found==0:
#                 util(m,s-i,arr,res)
#             arr.pop()
# def util_next(m,s,arr,res):
#     global found
#     if found==1:
#         return 
#     if len(arr)<=m and s>=0:
#         if len(arr)==m and s==0 and arr[0]!=0:
#             res.append(''.join([str(x) for x in arr]))
#             found = 1
#             return 
#         for i in range(0,10):
#             arr.append(i)
#             if found==0:
#                 util(m,s-i,arr,res)
#             arr.pop()
# #m,s = [int(x) for x in input().split()]
# m = 3
# s = 10
# res = []
# util(m,s,[],res)
# if len(res)<1:
#     print("-1 -1")
# else:
#     highest = res[0]
#     if highest[-1]=='0':
#         found = 0
#         util_next(m,s,[],res)
#         print(res)
#         if len(res)<2:
#             print(-1,highest)
#         else:
#             print(res[-1],highest)
#     else:
#         print(highest[::-1],highest)
m,s = [int(x) for x in input().split()]
# m= 2
# s=2

def can(m,s):
    return s>=0 and s<=9*m
#to_generate_minimum
res1= []
sumi = s
for i in range(0,m):
    for j in range(0,10):
        if (i > 0 or j > 0 or (m == 1 and j == 0)) and can(m - i - 1, sumi - j):
            res1.append(j)
            sumi -= j
            break
if s==0 and m>1:
    print(-1,-1)
else:
    if len(res1)==m:
        print(*res1,sep="",end=" ")
        res1= []
        sumi=s
        for i in range(0,m):
            for j in range(9,-1,-1):
                if (i > 0 or j > 0 or (m == 1 and j == 0)) and can(m - i - 1, sumi - j):
                    res1.append(j)
                    sumi -= j
                    break
        print(*res1,sep="")
    else:
        print(-1,-1)