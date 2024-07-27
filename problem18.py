# This is about removing the Duplicate elements in the List

# Method -1 Using Set method

arr = [5,4,13,7,9,1,3,7]


arr = list(set(arr))

print(arr)

# Method -2 Using List Comprehension  Enemurated method

test_list = [1, 5, 3, 6, 3, 5, 6, 1]
res = [i for n, i in enumerate(test_list) if i not in test_list[:n]]
print("The list after removing duplicates:", res)

# Method -3 Using LOrdered Dict

from collections import OrderedDict
test_list = [1, 5, 3, 6, 3, 5, 6, 1]
unique_list = list(OrderedDict.fromkeys(test_list))
print("The list after removing duplicates:", unique_list)

# Method -4 

test_list = [1, 3, 5, 6, 3, 5, 6, 1]
res = []
for x in test_list:
    if x not in res:
        res.append(x)
print("The list after removing duplicates:", res)

