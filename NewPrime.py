def NewPrime(x):
    if x < 4:
        return("Please enter an integer greater than 3")
    if type(x) != int:
        return("Please enter an integer value")
    else:
        primes = [2,3]
        for i in range(4,x+1):
            if isPrime(i) == 'Prime':
                primes.append(i)
        np = 1
        for j in range(0,len(primes)):
            np = np * primes[j]
        np = np + 1
        return(np)
