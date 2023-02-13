import timeit
t1 = timeit.default_timer()

sum = 0
for i in range(1010):
    sum += i
print(sum)

# t2 = timeit.default_timer()

# print("time in seconds:" , t2 - t1)
print("t1 is: ", t1)
# print("t2 is: ", t2)
