# word = input("Enter something: ")
# new_word = ""
# counter = 0
# for i in word:
#     counter += 1 
#     if i == " ":
#         print(new_word)
#         new_word = ""
#         continue
#     new_word += i
#     if counter == len(word)-1:
#         print(new_word)


# Create a list of the squares of numbers from 1 to 10 using a list comprehension.

# Create a list of numbers from 1 to 10 that are divisible by 3 using a list comprehension.

# d3_list = [x for x in range(1,11) if x % 3 == 0]

# Create a list of the first 10 even numbers using a list comprehension.
even_list = [i for i in range(1,22) if i % 2 == 0]

# Create a list of all the uppercase letters in the string "Hello, World!" using a list comprehension.
upper_list = [i for i in "Hello, World" if i in "ZXCVBNMASDFGHJKLQWERTYUIOP"]
# print(upper_list)

# Create a list of the lengths of the words in the string "The quick brown fox jumps over the lazy dog" using a list comprehension
len_list = [len(word) for word in "The quick brown fox jumps over the lazy dog".split()]
# print(len_list)

# Create a list of the squares of even numbers from 1 to 10 using a list comprehension.
my_list = [i**2 for i in range(2,21,2)]
# print(my_list)

# Create a list of all the vowels in the string "Hello, World!" using a list comprehension.
# vowels_list = [i for i in "Hello, World!" if i in "euoiaEUOIA"]
# print(vowels_list)

# Create a list of the sum of the elements in each tuple in the list [(1, 2), (3, 4), (5, 6)] using a list comprehension.
# typle_list = [tupl[0] + tupl[1] for tupl in [(1, 2), (3, 4), (5, 6)] ]
# print(typle_list)


# Create a list of the first 10 Fibonacci numbers using a list comprehension.
fibonacci = [0, 1]
[fibonacci.append(fibonacci[i]+fibonacci[i+1]) for i in range(0,8)]
# [fibonacci.append(fibonacci[i-1] + fibonacci[i-2]) for i in range(2, 10)]
print(fibonacci)

# Create a list of all the numbers from 1 to 10 that are not divisible by 2 and 3 using a list comprehension.
print([x for x in range(1,11) if x%2 != 0 and x%3 != 0])