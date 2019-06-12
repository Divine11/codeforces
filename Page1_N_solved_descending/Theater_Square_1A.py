# Theatre Square in the capital city of Berland has a rectangular shape with the size n × m meters. On the occasion of the city's anniversary, a decision was taken to pave the Square with square granite flagstones. Each flagstone is of the size a × a.

# What is the least number of flagstones needed to pave the Square? It's allowed to cover the surface larger than the Theatre Square, but the Square has to be covered. It's not allowed to break the flagstones. The sides of flagstones should be parallel to the sides of the Square.

# Input
# The input contains three positive integer numbers in the first line: n,  m and a (1 ≤  n, m, a ≤ 109).

# Output
# Write the needed number of flagstones.

n,m,a = [int(x) for x in input().split()]

n_tiles = 1
if n//a!=0:
    n_tiles = n//a
    if n%a!=0:
        n_tiles +=1
m -= a
if m==0:
    m_tiles = 0
else:
    m_tiles = 1
if m//a!=0:
    m_tiles = m//a
    if m%a!=0:
        m_tiles += 1
tiles = m_tiles+n_tiles+((n_tiles-1)*m_tiles)
print(tiles)
