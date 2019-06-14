# Let's consider a table consisting of n rows and n columns. The cell located at the intersection of i-th row and j-th column contains number i × j. The rows and columns are numbered starting from 1.

# You are given a positive integer x. Your task is to count the number of cells in a table that contain number x.

# Input
# The single line contains numbers n and x (1 ≤ n ≤ 105, 1 ≤ x ≤ 109) — the size of the table and the number that we are looking for in the table.

# Output
# Print a single number: the number of times x occurs in the table.

# Examples
# inputCopy
# 10 5
# outputCopy
# 2
# inputCopy
# 6 12
# outputCopy
# 4
# inputCopy
# 5 13
# outputCopy
# 0
# Note
# A table for the second sample test is given below. The occurrences of number 12 are marked bold.
n,x = [int(i) for i in input().split()]
# n = 5
# x = 13
res = 0
for i in range(1,n+1):
    if x%i==0 and x//i<n+1:
        res+=1

print(res)