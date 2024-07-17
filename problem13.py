#Lets see a vector

v = [2,-3,1]

print(4*v) #What happened here is 4*v= v+v+v+v when we try to multiply

a = [2,4,9]
b=[5,6,8]

print(a+b) #It will concatinate the string

#To multiply the vector we need to use a loop

w = [4*x for x in v]

print(w)