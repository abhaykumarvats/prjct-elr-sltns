#==============================================================================
# Problem 10: Summation of primes
#==============================================================================

def is_prime(number):
    """
    number: an integer
    returns: True if number is prime, False otherwise
    """
    
    # square root of number
    sqrtNumber = int(number**0.5)
    
    # for each prime in primes
    for prime in primes:
        # if current prime is greater than square root of number,
        # number is prime
        if prime > sqrtNumber:
            return True
        # else if number is divisible by a prime in primes list,
        # number is not prime
        elif not number % prime:
            return False

# first two primes
primes = [2, 3]
# sum of first two primes
sumOfPrimes = 5
# start finding primes from 5
number = 5

# find all the primes below 2 million
while number < 2000000:
    # if current number is prime
    if is_prime(number):
        # add it to primes list and sum
        primes.append(number)
        sumOfPrimes += number
    
    # update number for next iteration
    number += 2

# print final result
print("Answer:", sumOfPrimes)