#==============================================================================
# Problem 1: Multiples of 3 and 5
#==============================================================================

sum = 0
# for every number in the range [0, 1000)
for number in range(1000):
    # if the number is divisible by 3 or 5
    if number % 3 == 0 or number % 5 == 0:
        # add it to the sum
        sum += number

# print result
print("Answer:", sum)