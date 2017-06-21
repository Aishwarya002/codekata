low=input("enter a low value")
high=input("enter a high value")
while (low < high):
    flag = 0
    for i in range(2,low):
        if(low % i == 0):
            flag = 1
            break
    if (flag == 0):
        print(low)
        low=low+1
