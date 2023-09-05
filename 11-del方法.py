class Demo:
    def __init__(self, name):
        print('我是 __init__, 我被调用了 ')
        self.name = name

# __init__ 方法, 创建对象之后,会自动调用  (构造方法)
# __del__ 方法, 对象被删除销毁时, 自动调用的(遗言, 处理后事)  (析构方法)
# ​
# 1. 调用场景, 程序代码运行结束, 所有对象都被销毁
# 2. 调用场景, 直接使用 del 删除对象(如果对象有多个名字(多个对象引用一个对象),需要吧所有的对象都删除才行 )

    def __del__(self):
        print(f'{self.name} 没了, 给他处理后事...')


# Demo('a')

a = Demo('a')
b = Demo('b')
del a  # 删除销毁 对象,
print('代码运行结束')
