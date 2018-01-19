# PrimeChecker
Check if a number greater than 3 is prime only using odd numbers to 1/3 of the numbers value.
Except for two, all primes are odd and thus will only have odd factors.  Even numbers are automatically labeled compisite
by this function as all numbers will be initially checked to see if N%2 == 0.  If it is, we know that the number will not be prime since
it is greater than 3 and the only prime that has the property of N%2== 0 is 2 itself.
For an odd number, N, the biggest possible factor is N/3. This function does not run through all the numbers up to (N+1)/2 
but only odds to about N/3 with a bit of an overshoot to ensure all relevant numbers are checked.
