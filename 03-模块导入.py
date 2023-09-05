# # 方式一
# import 模块名
# # 使用模块中的内容
# 模块名.工具名
# ​
# # 举例
# import random
# import json
# random.randint(a, b)
# json.load()
# json.dump()
import random

print(random.randint(1, 20))

# # 方式二
# from 模块名 import 工具名
# # 使用
# 工具名  # 如果是函数和类需要加括号
# ​
# # 举例
# from random import randint
# from json import load, dump
# randint(a, b)
# load()
# dump()

# from random import randint
# from random import randint
#
# print(randint(1, 20))

# # 方式三, 问题: 可能存在多个模块中有相同的名字的工具, 会产生冲突
# from 模块名 import *  # 将模块中所有的内容都导入
# ​
# from random import *
# from json import *
# ​
# randint(a, b)
# load()
# dump()

# from random import *
#
# print(randint(1, 20))


# 对于导入的模块和工具可以使用 as 关键字给其起别名
# 注意: 如果起别名,原来的名字就不能用了, 只能使用别名

# 在导入模块的时候 会先在当前目录中找模块, 如果找到,就直接使用
# 如果没有找到回去系统的目录中进行查找, 找到,直接使用
# 没有找到, 报错
# ​
# 注意点:
# 定义代码文件的时候, 你的代码名字不能和你要导入的模块名字相同