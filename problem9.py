#This is not an Hacker Rank Problem I am learning List Comprehension

squares = []

for i in range(1,101):
    squares.append(i**2)

print(squares)

#This can be also solved in single line

square2 =[i**2 for i in range(1,101)]

print(square2)
