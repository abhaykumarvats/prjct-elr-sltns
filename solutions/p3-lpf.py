#==============================================================================
# Problem 3: Largest prime factor
#==============================================================================

def isPrime(number):
    """
    number: an integer
    returns: True if number is prime, False otherwise
    """
    
    # 1 is not prime
    if number == 1:
        return False
    # 2 and 3 are prime numbers
    elif number == 2 or number == 3:
        return True
    else:
        # check whether number is divisible by any other number in primes list
        for prime in primes:
            if number % prime == 0:
                # return False if it is divisible
                return False
        # if the number is prime, append it to primes list and return True
        primes.append(number)
        return True

# helper variables and data structures
primes = [2, 3]
givenNum = 600851475143
# square root of given number
sqrtNum = int(givenNum**0.5)

# for every number till square root of given number
for number in range(1, sqrtNum + 1):
    if givenNum % number == 0 and isPrime(number):
        # if the number is prime
        largestPrime = number

# print final result
print("Answer:", largestPrime)