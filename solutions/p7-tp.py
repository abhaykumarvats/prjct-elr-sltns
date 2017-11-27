#==============================================================================
# Problem 7: 10001st prime
#==============================================================================

def is_prime(number):
    """
    number: an integer
    returns: True if number is prime, False otherwise
    """
    
    # for each prime in primes
    for prime in primes:
        # if number is divisible by a prime in primes list,
        # return False
        if number % prime == 0:
            return False
    
    # if we have reached here, the number is prime, return True
    return True


# we know for sure that 2 and 3 are primes, so we are starting with them
primes = [2, 3]
# answer is initialised with 5 because 4 is definitely not prime
answer = 5

# start finding 10001st prime
while len(primes) < 10001:
    # if current value of answer is prime, append it to primes list
    if is_prime(answer):
        primes.append(answer)
    # increment answer by 2 for next iteration, we don't need even values
    answer += 2
#             ^here--<--<--<--<--<--<--<--<--<--<--<--<--<--<--<-
# print final answer after removing the extra 2 that we added --^
print("Answer:", answer - 2)