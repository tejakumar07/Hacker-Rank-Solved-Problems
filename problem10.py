remainders5 = [i**2 % 5 for i in range(1,101)]

print(remainders5)

remainders11 = [i**2%11 for i in range(1,101)]

print(remainders11)

#If we divide by using prime number we will see an intresting pattern
#p_remainders = [x**2 % p for x in range(0,p)]
#len(p_remainders) = p+1/2
#Called Quadratic reciprocity