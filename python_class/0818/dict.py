# dict以键值对的形式存储，基于 hash表实现,{key: value, key1: value1}
# -> key必须是可 hash的，不可变是可 hash的比要条件
# md5 / sha1 字符串 hash算法
a = {
    10: 'ten',
    'key': 'value',
    'key3': 100
}
for key in a:
    print(key, a[key])

# hash的线程安全问题





