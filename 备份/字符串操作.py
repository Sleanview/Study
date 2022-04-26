'''
序列：在python当中 序列就是一组按照顺序排列的值【数据组合】
在python中存在三种内置的序列类型：
字符串、列表、元组
优点：可以支持索引和切片的操作
特征：第一个正索引为0，指向的是左端，第一次索引为负数的时候，指向的是右端
切片是指截取字符串中的一段内容。
切片使用基本语法：
[起始下标：结束下标：步长] 步长是指隔几个下标获取一个字符。
可以根据下标来获取序列对象的任意 [ 部分 ] 数据
语法结构：[start:end:step] step默认1
'''

Test='python'
# print(type(Test))
# print('获取第一个字符%s'%Test[0])
# print('获取第二个字符%s'%Test[1])
# for item in Test:
#     print(item,end=' ')

name='peter'
# print('姓名首字母转换大写%s'%name.capitalize()) # 首字母变大写
a='    hello    '
# b=a.strip() # 去除字符串中两边的空格
# print(b)
# print(a)
# print(a.lstrip()) # 删除左边的空格
# print(a.rstrip()) # 删除右边的空格
# 复制字符串
# print('a的内存地址%d'%id(a)) # id函数 可以查看一个对象的内存地址
# b=a
# print('a的内存地址%d'%id(b))
# print(b)
dataStr='I love Python'
# print(dataStr.find('P')) # find函数可以查找目标对象在序列中的值，如果没找到就返回-1
# print(dataStr.index('o')) # 检测字符串中是否包含子字符串 返回的是下标值
# index找不到报异常，find找不到返回-1
# print(dataStr.startswith('I')) # 判断
# print(dataStr.endswith('I'))

# print(dataStr.lower()) # 小写
# print(dataStr.upper()) # 大写

strMsg='hello world'
# slice [start:end:step] 左闭右开  strat<=value<end
# print(strMsg) # 输入完整的数据
# print(strMsg[0])
print(strMsg[2:5]) # 2-5下标之间的数据
print(strMsg[2:]) # 第三个字符串到最后
print(strMsg[:3]) # 1-3     print(strMsg[0:3])=print(strMsg[:3])
print(strMsg[::-1]) # 倒序输出  负号表示方向   从右边往左去遍历

# 共有方法  +  *  in
# 字符串合并
strA='人生苦短'
strB='我用python'
# list 合并
listA=list(range(10))
listB=list(range(11,20))
print(listA+listB)
# print(strA+strB)
# 复制 *
# print(strA*3)
# print(listA*3)
# in 对象是否存在 结果是一个bool值
print('生'in strA) # Ture
print(22 in listA) # False
dictA={'name':'peter'}
print('name' in dictA)