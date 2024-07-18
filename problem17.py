#In this problem lets try to find the Maximum number and Minimum number in the list


#This can be solved using two ways

#Method-1 Using Sort Method

my_list = [515,15,65,7,656,766,968,1534,77,265,9]

my_list.sort()

print("The Smallest number in the List is:",my_list[0])

print("The largest number in the list is:",my_list[-1])

#Method-2 Using the direct methods

my_list1 = [7,56,65,94,58,65,22,64]


print("The smallest number in list1 is:",min(my_list1))

print("The laargest number in list1 is:",max(my_list1))