def isPrime(x):
#checks to see  whether a number greather than 3 is prime or composite    
    
    y = x+1
    z = x+2
    c = 0
    if x < 4:
        print("Please enter an integer greater than 3")
    if type(x) != int:
        print("Please enter an integer value")
    else:
        if x%2 == 0:
            c = c + 1

        elif x%3 == 0:
            c = c+1

        elif((x+1)%3 == 0):
            m = int((x+1)/3)
            if m%2 == 0:
                n = int(m/2)
                for i in range(1,n+1):
                    if x%(2*i+1) == 0:
                        c = c + 1
            elif m%2 != 0:
                n = int((m+1)/2)
                for i in range(1,n+1):
                    if x%(2*i+1) == 0:
                        c = c + 1
        elif((x+2)%3 == 0):
            m = int((x+2)/3)
            if m%2 == 0:
                n = int(m/2)
                for i in range(1,n+1):
                    if x%(2*i+1) == 0:
                        c = c + 1
            elif m%2 != 0:
                n = int((m+1)/2)
                for i in range(1,n+1):
                    if x%(2*i+1) == 0:
                        c = c + 1

        if c == 0:
            return('Prime')
        else:
            return('Composite')
