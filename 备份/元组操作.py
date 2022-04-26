'''
元组：是一种不可变的序列，在创建后不能做任何修改
1：不可变
2：用（）创建元组序列，数据项用逗号来分割
3：可以是任何的类型
4：当元组中只有一个元素时，要加上逗号，不然解释器会当作整形来处理
5：同样支持切片操作
'''
# 元组的创建 不能进行修改
tupleA=() # 空元组
print(id(tupleA))
tupleA=('abcd',89,9.12,'peter',[11,22,33])
# print(id(tupleA))
# print(type(tupleA))
# print(tupleA)
# 元组的查询
# for item in tupleA:
#     print(item,end=' ')
# print(tupleA[2:4])

# print(tupleA[::-2]) # 表示反转字符串，每隔两个取一次
# print(tupleA[::-3]) # 表示反转字符串，每隔三个取一次
# print(tupleA[-2:-1]) # 倒着取下标为-2到-1区间的
# print(tupleA[-4:-2]) # 左闭右开 注：左边的数一定小于右边的数，否则取值为空

# tupleA[0]='pythonhello' # 错误
# tupleA[4][0]=283425  # 可以对元组中的列表进行修改
# print(tupleA)

tupleB=('1',)# 当元组中只有一个数据项的事故后，必须要在第一个数据项后面加上逗号
# print(type(tupleB))
tupleC=(1,2,3,4,3,4,4,1)# tuple(range(10))
print(tupleC.count(4)) # count可以统计元素出现的次数