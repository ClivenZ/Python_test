#help(list)

'''
a = [9, 5, 2, 7]
b = [3, 4, 5]
a.append(b)
a.extend(b)
print(a)
'''

# a = [10, 20, 30, 40]
# a.append(50)
# a.pop(0)
# print(a)


#浅拷贝
a = [1, 3, 5, 7]
b = [2, 4, 6, 8]
a = b
a[0] = 100
print(a, b)
print(id(a), id(b))

#深拷贝(只能针对可变对象使用)
import copy
a = [1, 3, 5, 7]
b = [2, 4, 6, 8]
b = copy.deepcopy(a)
a[0] = 100
print(a, b)
print(id(a), id(b))
