
# # ex1:
# for i in range(1,11):
#     print(i, end=",")

# # ex2:
# sum=0
# for i in range(1,101):
#     sum += i
# print(" -> ex2: ",sum)

#  ex3:
# for i in range(1,21):
#     if i%2 == 0:
#         print(i, end=",")

# ex4:
# num = int(input("Enter number:"))
# for i in range(1,num+1):
#         print(i*num,end=",")

# # ex 5:
# my_list = [1,2,6,9,"ooowoo"]
# for element in my_list:
#     print(element)

# x = ""
# num = int(input("enter num:"))
# for i in range(num):
#     x += "*"
#     print(x)


# ------harder Q`2-----

# Q1:
# n = 5
# n1 = 0
# n2 = 1
# print(n1,",",n2,end=",")
# for i in range(n-2):
#     sum = n1+n2
#     print(sum,end=",")
#     n1 = n2 
#     n2 = sum

# # Q2: find prime number
# num1 = 2
# num2 = 13
# for i in range(num1,num2+1): # Loops through all the numbers in the given range
#     prime_number = True
#     for j in range(2,i): # Checks whether the number is divisible other than by itself and by one
#         if i%j == 0:
#             prime_number = False
#             break
#     if prime_number == True:
#         print(i)

# Q3: fix the bugs
# numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for lst in numbers:
#     for num in lst:
#         print(num)

# Q4:  Flattening a nested list
# numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flat_list = []
# for lst in numbers:
#     for num in lst:
#         flat_list.append(num)  
# print(flat_list)

# Q5: frequency of each element
numbers = [1, 2, 3, 4, 2, 1, 4, 4, 5, 1]
freq = {}
for num in numbers:
    counter = 0
    for i in numbers:
        if num == i:
            counter += 1
    freq[num] = counter
print(freq)


