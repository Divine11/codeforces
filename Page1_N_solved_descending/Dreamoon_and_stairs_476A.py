# Dreamoon wants to climb up a stair of n steps. He can climb 1 or 2 steps at each move. Dreamoon wants the number of moves to be a multiple of an integer m.

# What is the minimal number of moves making him climb to the top of the stairs that satisfies his condition?

# Input
# The single line contains two space separated integers n, m (0 < n ≤ 10000, 1 < m ≤ 10).

# Output
# Print a single integer — the minimal number of moves being a multiple of m. If there is no way he can climb satisfying condition print  - 1 instead.
def no_of_moves(n,m):
    x = n//2
    while x>0 and (n-x)%m!=0:
        x-=1
    y = n-(2*x)
    if (n-x)%m==0:
        return x+y
    else:
        return -1
n,m = [int(i) for i in input().split()]
# n = 3
# m = 5
print(no_of_moves(n,m))
