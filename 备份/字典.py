'''
字典：也是python中重要的数据类型，字典是由 键值对 组合的集合，通常使用键来访问数据，效率非常高，和list一样 支持对数据的添加、修改、删除

特点：
1：不是序列类型 没有下标的概念，是一种无序的键值集合，是内置的高级数据类型
2：用{} 来表示字典对象，每个键值对用逗号分隔
3：键 必须是不可变的类型【元组、字符串】值可以是任意的类型
4：每个键必定是唯一的，如果存在重复的键，后者会覆盖前者
'''
# 如何创建字典、
dictA={'种族':'食人种','From':'Xenoblade2'} # 空字典
# 添加字典数据
dictA['name']='Nia'   # key:value
dictA['age']='16'
dictA['pos']='异刃'

# 结束添加
# print(dictA) # 输出完整的字典
# print(len(dictA))   # 数据项长度
# print(type(dictA))

# print(dictA['name']) # 通过键获取对应的值
# dictA['name']='Mio' # 修改键对应的值
# dictA['From']='Xenoblade3'
# dictA.update({'age':20})
# dictA.update({'height':1.60})  # 可以添加或更新
# print(dictA)

# 获取所有的键
# print(dictA.keys())
# 获取所有的值
# print(dictA.values())
# 获取所有的键和值
# print(dictA.items())

# for key,value in dictA.items():
#     print('%s==%s'%(key,value))

# 删除操作
# del dictA['name'] # 通过指定键进行删除
# dictA.pop('age') # 通过指定键进行删除
print(dictA)
#  如何排序 按照key排序
print(sorted(dictA.items(),key=lambda d:d[0]))
# 按照value排序
print(sorted(dictA.items(),key=lambda d:d[1]))

'''
key是函数sorted内的一个参数，用来指定排序方式
key=lambda d:d[] 是一个排序方法
对于现在的例子，d:d[0] 表示按照key的内容排序
d:d[1] 表示按照value的内容排序
sort和sorted的区别是，sort是对原始数据的排序
即执行过sort过后，原来的数据排序进行改变
而sorted相当于复制了一个副本，对副本进行排序，不影响原始数据
'''