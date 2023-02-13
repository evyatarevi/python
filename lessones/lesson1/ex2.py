# first_name = input("enter your first name:")
# last_name = input("Enter your last name:")
# age = input("Enter your age:")
# height = input("Enter your height:")

# print(type(age,))
# print(int(age)+10)

#ex3
# num = int(input("Enter number: "))
# print(num**2)

#ex4

# num = int(input("Enter number: "))
# dig1 = num%10
# dig2 = num//10 % 10
# dig3 = num//100 
# print(dig1+dig2+dig3)
# print(num//10)

# # ex5
# num = input("Enter number: ")
# length = len(num)
# num = int(num)
# sum = 0
# for index in range(length):
#     sum += num%10
#     num = num // 10

# print(sum)

# ex6
# import random
# num = random.randint(0,10)
# guss = int(input("guss number betwen 0-10: "))
# if (num == guss):
#     print("you win!")
# else:
#     print("so close! your distans from the number ",num," is: ",num-guss) 

# carps
import random
dice1 = random.randint(1,6) 
dice2 = random.randint(1,6) 
s = dice1 + dice2 
print(s)
if(s == 7 or s == 11):
    print("you win!")
elif(s == 2 or s == 3 or s == 12):
        print("you los...")

else: 
    index = True
    count = 1
    while index:
        count += 1
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        s2 = dice1 + dice2
        print(s2)
        if(s == s2): 
            print("you win in the ",count," round")
            index = False
        elif(s2 == 7): 
            print("you loossse in the ",count," round")
            index = False

    
