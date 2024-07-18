#This is the Hacker rank Problem
#https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true
#This problelm can be solved using loops aswell as list comprehensions

#This is method to solve using loops
x = int(input())

y = int(input())

z = int(input())

n = int(input())

l = []

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if (i+j+k !=n):
                l.append([i,j,k])

print(l)