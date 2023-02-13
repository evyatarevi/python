"""
Write a function that takes a string as input and returns a string with all vowels removed.

Write a function that takes a number as input and returns its factorial.

3. Write a function that takes two lists of equal length as input and returns a new list containing 
the elements of both lists, alternating between the two.


4. Write a function that takes a string as input and returns the number of times a specific character appears
 in the string.

5.Write a function that takes a number as input and returns its Fibonacci sequence up to that number.

6.Write a function that takes a list of numbers as input and returns the largest number in the list.

7.Write a function that takes a string as input and returns a string with all vowels replaced with 'x'.

8.Write a function that takes a list of numbers as input and returns the sum of all the even numbers in the list.

9.Write a function that takes two strings as input and returns a string with the first string repeated the number 
of times specified by the second string.

10.Write a function that takes a list of numbers as input and returns a new list with all duplicates removed

"""

# Write a function that takes a string as input and returns a string with all vowels removed.

# def rem_vow(mystr):
#     vowels='aeiouAEIOU'
#     mylist = []
#     for i in mystr:
#         if i not in vowels:
#             mylist.append(i)
#     return "".join(mylist)

# print(rem_vow("pokemon"))



# Write a function that takes a number as input and returns its factorial.

# def factor(num):
#     factori = 1  
#     for i in range(num+1):
#         if i == 0:
#             continue
#         factori *= i
#     return factori
# print(factor(5))


# # Write a function that takes two lists of equal length as input and returns a new list containing the elements of both lists, alternating between the two.
# def lists(list1, list2):
#     new_list = []
#     for i in list1:
#         new_list.append[list1[i]]
#         new_list.append[list2]
#     return new_list
# print(lists([1,3,5],[2,4,6]))


# # 3.
# def altern(list1,list2):
#     new_list = []
#     for i in range(len(list1)):
#         new_list.append(list1[i])
#         new_list.append(list2[i])
#     return new_list
# print(altern([1,3,5],[2,4,6]))

# # 4.
# def times(str,c):
#     counter = 0
#     for x in str:
#         if x == c:
#             counter += counter
#     return counter

# 5
# def up_fibo(number):
#     num1=0
#     num2=1
#     print(0)
#     num3 = num1 + num2
#     while(num3 <= number):
#         print(num3)
#         num3= num1 + num2
#         num1=num2
#         num2=num3
    
# up_fibo(20)

# # 6.
# def largest(get_list):
#     largest_num = get_list[0]
#     for i in range(1,len(get_list)-1):
#         if get_list[i] > largest_num: 
#             largest_num = get_list[i]
#         # print(largest_num,"\n-----")  documention
#     return largest_num
# print(largest([1,4,24,3,10,44,8]))

# # 7
# def val_x(str):
#     new_str = ""
#     for char in str:
#         if char in "euioaEUIOA":
#             new_str += "x"
#         else:
#             new_str += char
#     return new_str
# print(val_x("hello world euIOda"))

# # 8
# def sum_list(list):
#     sum = 0
#     for x in list:
#         if x%2 == 0:
#             sum += x
#     return sum

# print(sum_list([1,2,4,1,5,4,2]))

# 9
def no_diplcated(list):
    for i in range(1,len(list)):
        if list[0] == list[i]:
            list.pop(i)
            [].pop
            
            
