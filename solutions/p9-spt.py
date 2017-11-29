#==============================================================================
# Problem 9: Special Pythagorean triplet
#==============================================================================

# flag
found = 0

# a lies in [1, 500)
for a in range(1, 500):
    # b lies in [a + 1, 500)
    for b in range(a + 1, 500):
        # c lies in [b + 1, 500)
        for c in range(b + 1,  500):
            # a < b < c is satisfied with these three loops
            if (a + b + c) == 1000 and (a**2 + b**2) == c**2:
                # when the combination is found,
                # break out of all the loops sequentially,
                # using flag "found"
                found = 1
                break
        if found:
            break
    if found:
        break
                
# print final result
print("Answer:", a * b * c)