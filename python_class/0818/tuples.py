#元组不可修改（只读）
a = (10, 20, 30, 40, 50)
#a = (10)  -> type(a) = int
#a = (10,) -> type(a) = tuple

def get_point():
    return 10, 20
tmp = get_point()
#print(tmp, type(tmp))

# tuple的使用场景：
#   函数传参的时候使用元组可以避免函数内部把函数外部的内容修改掉
#   tuple是可 hash的，元组就可以作为字典的 key，而 list不行
a = (1, 2, 3)
b = {
    a: 100
}
print(type(b))



