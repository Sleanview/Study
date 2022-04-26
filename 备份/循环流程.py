# 循环的分类
# while 语法结构
# while 条件表达式:
#     代码指令
# 语法特点
# 1.初始值
# 2.条件表达式
# 3.变量【循环体内计数变量】的自增或自减，否则会造成死循环
# 使用条件：循环次数不确定，是依靠循环条件来 结束
# 目的；使代码更加简洁，可重复利用
# for

# while的使用
# 输出1~100间的数据
# index=0 #定义一个变量
# while index>=100:
#     print(index)
#     index-=2
# 打印九九乘法表 循环的嵌套
# row=9
# while row>=1:
#     col=1
#     while col<=row:
#         print('%d*%d=%d'%(row,col,row*col),end=' ')
#         col+=1
#         pass
#     print()
#     row-=1
#     pass
# 打印直角三角形
# row=1
# while row<=7:
#     j=1
#     while j<=row:
#         print('*',end=' ')
#         j+=1
#         pass
#     print()
#     row+=1
# 方向相反的直角三角形
# row=7
# while row>=1:
#     j=1
#     while j<=row:
#         print('*',end=' ')
#         j+=1
#         pass
#     print()
#     row-=1
# 等腰三角形
# row=1 # 控制行数的变量
# while row<=10:
#     j=1
#     while j<=10-row: # 控制打印空格的数量，这里的5对应横竖空格
#         print('.',end='')
#         j+=1
#         pass
#     k=1
#     while k<=2*row-1: #控制打印*号
#         print('*',end='')
#         k+=1
#         pass
#     print()
#     row+=1

# for 循环
# 语法特点：遍历操作，依次的取集合容器中的每个值
# for 临时变量 in 容器
#     执行代码块

# tags='我是蝙蝠侠' # 字符串类型本身就是一个字符类型的集合
# for item in tags:
#     print(item)

# range 此函数可以生成一个数据集合列表
# range(起始：结束：步长) 步长不能为0
# sum=0
# for data in range(1,101): # 左包含右不包含
#     print(data,end=' ') # end 不让它换行，用空格来分割一下
#     sum+=data #求累加和
#     # print(data,end=' ')
#     pass
#
# print('sum=%d'%sum)
# print('-----------------------for的使用--------------------------')
# for data in range(50,201):
#     if data%2==0: # 意思是除二没有余数
#         print('%d是偶数'%data)
#     else:
#         print('%d是奇数'%data)

# break和continue
# break 代表中断结束
# continue:结束本次循环，继续进行下次循环

# sum=0
# for item in range(1,51):
#     print(item)
#     if sum>100:
#         print('循环执行到%d就退出来了'%item)
#         break # 退出循环体
#     sum+=item

# # print('sum=%d'%sum)
# print('continue的使用')
# for item in range(1,100): # 求出奇数
#     if item%2==0:
#         continue
#         pass
#     print(item)
#     pass

# for item in 'I love python':
#     # if item=='e':
#     #     break
#     if item=='o':
#         continue
#     print(item,end=' ') # 为什么不包括e，因为break退出了for循环，自然不会运行最后的print(item)

index=1
while index<=100:
    if index>20:
        break
        pass
    print(index)
    index+=1

# while使用：适用于对未知的循环次数 用于判断
# for使用：适用于对已知的循环次数【可迭代对象遍历】