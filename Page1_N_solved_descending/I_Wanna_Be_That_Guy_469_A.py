# There is a game called "I Wanna Be the Guy", consisting of n levels. Little X and his friend Little Y are addicted to the game. Each of them wants to pass the whole game.
#
# Little X can pass only p levels of the game. And Little Y can pass only q levels of the game. You are given the indices of levels Little X can pass and the indices of levels Little Y can pass. Will Little X and Little Y pass the whole game, if they cooperate each other?
#
# Input
# The first line contains a single integer n (1 ≤  n ≤ 100).
#
# The next line contains an integer p (0 ≤ p ≤ n) at first, then follows p distinct integers a1, a2, ..., ap (1 ≤ ai ≤ n). These integers denote the indices of levels Little X can pass. The next line contains the levels Little Y can pass in the same format. It's assumed that levels are numbered from 1 to n.
#
# Output
# If they can pass all the levels, print "I become the guy.". If it's impossible, print "Oh, my keyboard!" (without the quotes).
#
# Examples
# inputCopy
# 4
# 3 1 2 3
# 2 2 4
# outputCopy
# I become the guy.
# inputCopy
# 4
# 3 1 2 3
# 2 2 3
# outputCopy
# Oh, my keyboard!
# Note
# In the first sample, Little X can pass levels [1 2 3], and Little Y can pass level [2 4], so they can pass all the levels both.
#
# In the second sample, no one can pass level 4.
n = int(input())
x = [int(x) for x in input().split()]
y = [int(y) for y in input().split()]
x = x[1:]
y = y[1:]
x.sort()
y.sort()
nx = len(x)
ny = len(y)
cur_level = 1
ix=0
iy=0
pass1 = True
while cur_level<=n:
    #print(cur_level,ix,nx,x[ix],iy,ny,y[iy])
    if ix<nx and iy<ny and x[ix]==y[iy] and x[ix]==cur_level:
        ix+=1
        iy+=1
        cur_level+=1
    elif ix<nx and x[ix]==cur_level:
        ix+=1
        cur_level+=1
    elif iy<ny and y[iy]==cur_level:
        iy+=1
        cur_level+=1
    else:
        print("Oh, my keyboard!")
        pass1 = False
        break
if pass1:
    print("I become the guy.")
