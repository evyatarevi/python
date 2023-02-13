def sorted(list1, list2):
    list3 = []
    while list1 and list2:
        if list1[0] <= list2[0]:
            list3.append(list1[0])
            list1.pop(0)
        else:
            list3.append(list2[0])
            list2.pop(0)
    if list1:
        list3.extend(list1)
    if list2:
        list3.extend(list2)
    return list3

print(sorted([1,3,5,8],[2,4,8,12,556,1333]))

