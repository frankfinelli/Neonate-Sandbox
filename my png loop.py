a = 53
while (a < 50000):
    b = 2
    while(b <= (a/b)):
        if not(a%b):
            break
        b += 1
    if (b > a/b):
        print (a)
    a += 2  

