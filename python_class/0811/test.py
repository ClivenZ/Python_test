'''
#变量和赋值
num = 10
pi = 3.141592653
name = 'wang'

#格式化字符串
num = 10
a = 'num = %d' % num
print(a)
a = 'num = {}'.format(num)
print(a)
a = f'num = {num}'
print(a)

#i/o
a = 'name'
print(a,end='') #不换行

a = input("Enter num:") #str格式
print(a)

print(2 ** 8)
'''

'''
#list 列表 可变对象
a = [9, 5, 2, 7]
print(len(a))

#tuple 元组 不可变对象
b = (9, 5, 2, 7)
print(len(b))

#dirt 字典 键值对 哈希表
a = {
    'ip':'127.0.0.1',
    'port':'80'
}
print(a['ip'])
'''
'''
#while
num = 0
while num < 10:
    print(num, end='')
    num += 1

#for
for num in range(0, 10):
    print(num, end='')
'''
# #列表解析
# a = [1, 2, 3, 4, 5, 6]
# b = []
# for num in a:
#     num = num * num
#     b.append(num)
# print(b)
#
# a = [1, 2, 3, 4, 5, 6]
# c = [num ** 2 for num in a]
# print(c)

# #函数
# def Add(x, y):
#     return x + y
# def Add(x, y, z = 0):
#     return x + y + z
# print(Add(10,2.1))
# print(Add('hello', 'world'))
# #不支持函数重载，后者覆盖前者,可以缺省
#
#
# #可以返回多个参数
# def Get_Point():
#     x = 10
#     y = 20
#     return x,y
# print(type(Get_Point))
#

# #文件操作
# f = open('S:/test.txt', 'r')
# for line in f:
#     print(line, end='')
# f.colse()
#
# f = open('S:/test.txt', 'r')
# lines = f.readlines()
# print(lines)
# f.close()
# #

# f = open('S:/test.txt', 'r')
# word_dict = {}
# for word in f:
#     word = word.strip() #去除字符串两侧的空白符号
#     if word_dict in word:
#

# import test2
#
# def Add(x, y, z):
#     return x + y + z
#
# print(test2.Add(10,20))
#

