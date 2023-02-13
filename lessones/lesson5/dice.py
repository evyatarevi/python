import random

# def calculat(get_list):
#     my_cal = []
#     while get_list:
#         num = get_list[0]
#         counter = 0
#         i = 0
#         while i < len(get_list):
#             if get_list[i] == num:
#                 counter += 1
#                 get_list.pop(get_list[i])
#                 continue
#             i += 1
#         my_cal.append({num:counter})
#         for i in range(len(get_list)):
#              if get_list[i] == num:
#                 get_list.remove(num) 
#         print(get_list)
#     return my_cal

# print(calculat([1,2,3,2,1,1]))

        

# sum = []
# while True:
#     if not input("please enter to continue or else key to stop: "):
#         x1 = random.randint(1,6)
#         x2 = random.randint(1,6)
#         print("-----")
#         print(x1,x2)
#         print("-----")
#         sum.append(x1+x2)
#     else:
#         calculat(sum)
#         print("by by!")
#         break
get_list = [1,1,2,2,3]

while get_list:
    num = get_list[0]
    counter = 0
    i = 0
    while i < len(get_list):
        if get_list[i] == num:
            counter += 1
            get_list.pop(i)
            continue
        i += 1
        print({num:counter})

