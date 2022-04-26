# 输出 %占位符
# me='我的'
# classPro='某高中一年6班'
# age=10
# print('%s名字是小明：来自【%s】，今年%d岁了。'%(me,classPro,age))
# print('%s名字是胖虎：来自【%s】，今年%d岁了。'%(me,classPro,age))
# print('%s名字是小叮当：来自【%s】，今年%d岁了。'%(me,classPro,age))
# %做占位符，%后面跟的是变量的类型 例如s(str)
# Name='lilei'
# Age=18
# print('我是%s，我的年龄的%d'%(Name,Age))
# Enemy='奥丁'
# Player='龙骑'
# print('你无法战胜%s，%s'%(Enemy,Player))
# print('我可以\n换行吗') # \n换行效果
'''
%s,%d,%f是常用的格式化符号
s字符串，d有符号的十进制整数，f浮点实数
'''

# 输出练习
"""
姓名：老夫子
QQ：66666
手机号：12138
公司地址：快乐老家
"""

# name='老夫子'
# QQ='66666'
# phone='12138'
# addr='快乐老家'
# # print('姓名：%s\nQQ:%s\nphone:%s\naddr:%s'%(name,QQ,phone,addr))
# # 格式输出的其他方式 .format()
# print('姓名：{},年龄是{}岁。'.format(name,23))
# print('姓名：{}\nQQ:{}\nphone:{}\naddr:{}'.format(name,QQ,phone,addr))
# print('-----------------以上是format形式的-------------------')

# 输入 input的练习 获取键盘输入的内容
name=input('请输入您的姓名：')
age=int(input('请输入您的年龄：'))
QQ=input('请输入您的QQ：')
phone=input('请输入您的电话：')
addr=input('请输入您的地址：')
print('姓名：%s\nage:%d\nQQ:%s\nphone:%s\naddr:%s'%(name,age,QQ,phone,addr))
# print('姓名：{}\nQQ:{}\nphone:{}\naddr:{}'.format(name,QQ,phone,addr))