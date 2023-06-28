for x in range(100,1000):
    sum=0
    first = x //100
    second = (x//10) % 10
    third = x % 10 
    sum = first**3+second**3+third**3
    if sum==x:
        print(x)