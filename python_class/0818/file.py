# a = open('d:/test.txt', 'r')

'''
with open('s:/text.txt', 'r', encoding='utf-8') as f:
    # print(f.readlines())
    for line in f:
        print(line)
'''
'''
with open('s:/text.txt', 'w',encoding='utf-8') as f:
    f.write('asd')
'''
#文件系统的基础操作
import os.path
path = 's:/asas/sasa/xxx.txt'
print(os.path.basename(path))

result = 's:/asas/sasa/'
print(os.path.abspath(result))
#路径和文件名分隔开
print(os.path.split(path))
#获取文件扩展名
print(os.path.splitext(path))

