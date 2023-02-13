# import random
# while True:
#     if random.randint(1,10) == int(input("Enter num: ")):
#         print("good choise!")
#         break
#     else:
#         print("Try again")


# def is_semmetric(num):
#     str1 = str(num)
#     for i in range(len(str1)):
#         if (str1[i] != str1[len(str1)-1-i]):
#             return False
#     return True

# print(is_semmetric(31213))


def multi_table():
    for i in range(1,11):
        for j in range(1,11):
            print(j,end=" ")
            print(i*j,end=" | ")
        print()

multi_table()
