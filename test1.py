while True:
        a=int(input())
        if(a<=0):
            break
        else:
            for i in range(1,a+1):
                if (a%i==0):
                    print(i,end=" ")
        print("")