# You are a lover of bacteria. You want to raise some bacteria in a box.

# Initially, the box is empty. Each morning, you can put any number of bacteria into the box. And each night, every bacterium in the box will split into two bacteria. You hope to see exactly x bacteria in the box at some moment.

# What is the minimum number of bacteria you need to put into the box across those days?

# Input
# The only line containing one integer x (1 ≤ x ≤ 109).

# Output
# The only line containing one integer: the answer.

def bacteria_count(num):
    count = 0
    while num>0:
        num = num&(num-1)
        count+=1
    return count

print(bacteria_count(int(input())))