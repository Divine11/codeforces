# Polycarpus has a ribbon, its length is n. He wants to cut the ribbon in a way that fulfils the following two conditions:
#
# After the cutting each ribbon piece should have length a, b or c.
# After the cutting the number of ribbon pieces should be maximum.
# Help Polycarpus and find the number of ribbon pieces after the required cutting.
#
# Input
# The first line contains four space-separated integers n, a, b and c (1 ≤ n, a, b, c ≤ 4000) — the length of the original ribbon and the acceptable lengths of the ribbon pieces after the cutting, correspondingly. The numbers a, b and c can coincide.
#
# Output
# Print a single number — the maximum possible number of ribbon pieces. It is guaranteed that at least one correct ribbon cutting exists.
#
# Examples
# inputCopy
# 5 5 3 2
# outputCopy
# 2
# inputCopy
# 7 5 5 2
# outputCopy
# 2
# Note
# In the first example Polycarpus can cut the ribbon in such way: the first piece has length 2, the second piece has length 3.
#
# In the second example Polycarpus can cut the ribbon in such way: the first piece has length 5, the second piece has length 2.
n,a,b,c = [int(x) for x in input().split()]
dp = [0]*(n+1)
dp[0] = 0
res = [a,b,c]
res.sort()
A = res[0]
B = res[1]
C = res[2]
for i in range(1,n+1):
    if i>A:
        if dp[i-A]!=0 and dp[i-B]!=0 and dp[i-C]!=0:
            dp[i] = max(1+dp[i-B],1+dp[i-C])
        elif dp[i-B]!=0:
            dp[i] = 1 + dp[i-B]
        elif dp[i-C]!=0:
            dp[i] = 1 + dp[i-C]
        else:
            dp[i] = 0
        dp[i] = max(1+dp[i-A],1+dp[i-B],1+dp[i-C])
    elif i>B:
        if dp[i-B]!=0 and dp[i-C]!=0:
            dp[i] = max(1+dp[i-B],1+dp[i-C])
        elif dp[i-B]!=0:
            dp[i] = 1 + dp[i-B]
        elif dp[i-C]!=0:
            dp[i] = 1 + dp[i-C]
        else:
            dp[i] = 0
    elif i>C:
        if dp[i-C] != 0:
            dp[i] = 1+dp[i-C]
        else:
            dp[i] = 0
    else:
        dp[i] = 0
print(dp[1:])