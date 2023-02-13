#     Write a program to convert the first letter of a string to uppercase.
x="evi"
print(x.capitalize())

#     Write a program to count the number of occurrences of a substring in a string.
str="evi if t"
print(len(str.split()))


#     Write a program to check if a string starts with a specific substring.

str="evi if t"
if_str = "evi"
check = True
for i in range(len(if_str)):
    if str[i] != if_str[i]:
        check = False
print(check)

#     Write a program to check if a string ends with a specific substring.
str="evi if rt"
if_str = "rt"
check = True
for i in range(len(if_str)):
    if str[-i-1] != if_str[-i-1]:
        check = False
print(check)


#     Write a program to find the index of a substring in a string.
str="evi if rt"
if_str = "if"
check = False
for i in range(len(str)):
    if str[i] == if_str[0]:
        check = True
        for j in range(len(if_str) -1):
            if if_str[j+1] != str[i+1+j]:
                check = False
        if check:
            print(i)
if not(check):
    print("the substring isn't existe")



#     Write a program to split a string into a list based on a specific character.
char = input("Enter char split")
str = "evyatar"
print(str.split(char))

#     Write a program to replace a specific substring in a string.
str = "evyatar"
old_input = input("Enter old char: ")
new_input = input("Enter new char: ")
str.replace(old_input, new_input)

#     Write a program to check if a string is alphanumeric.
my_input = input("Enter: ")
print(my_input.isalpha())

#     Write a program to check if a string is alphabetic.
my_input = input("Enter: ")
print(my_input.i)

#     Write a program to check if a string is numeric.

#     Write a program to check if a string is lowercase.

#     Write a program to check if a string is uppercase.

#     Write a program to strip whitespace from the beginning and end of a string.
print("  b   ".strip())
