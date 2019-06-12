n = int(input())
while n>0:
    temp = input()
    if len(temp)<=10:
        print(temp)
    else:
        print(temp[0]+str(len(temp)-2)+temp[-1])
    n-=1