# A. Combination Lock
# time limit per test2 seconds
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# Scrooge McDuck keeps his most treasured savings in a home safe with a combination lock. Each time he wants to put there the treasures that he's earned fair and square, he has to open the lock.


# The combination lock is represented by n rotating disks with digits from 0 to 9 written on them. Scrooge McDuck has to turn some disks so that the combination of digits on the disks forms a secret combination. In one move, he can rotate one disk one digit forwards or backwards. In particular, in one move he can go from digit 0 to digit 9 and vice versa. What minimum number of actions does he need for that?

# Input
# The first line contains a single integer n (1 ≤ n ≤ 1000) — the number of disks on the combination lock.

# The second line contains a string of n digits — the original state of the disks.

# The third line contains a string of n digits — Scrooge McDuck's combination that opens the lock.

# Output
# Print a single integer — the minimum number of moves Scrooge McDuck needs to open the lock.

# Examples
# inputCopy
# 5
# 82195
# 64723
# outputCopy
# 13

def no_of_steps(start,end,n):
    res = 0
    for i in range(n):
        st = int(start[i])
        en = int(end[i])
        res += min((st-en)%10,(en-st)%10)
    return res

n = int(input())
start = input()
end = input()
print(no_of_steps(start,end,n))
