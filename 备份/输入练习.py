# name=input('请输入您的姓名：')
# # age=int(input('请输入您的年龄：'))
# # QQ=int(input('请输入您的QQ；'))
# # addr=input('请输入您的住址；')
# # print('姓名：%s\n年龄：%d\n QQ：%d\n住址；%s'%(name,age,QQ,addr))

# num=int(input('你觉得TA心里想的数字是什么:'))
# num1=5
# print(type(num1))
# print(num == num1)
# if num==num1: #判断
#     print('恭喜你，你们可以结婚了')
#     pass
# else:
#     print('虽然很遗憾，但还是杀了TA比较好')
#     pass

# #猜拳击小游戏(改-五局三胜制)
# # 0：石头 1：剪刀 2：布
# import random #直接导入，产生随机数的模块
# #计算机 人
# count= 1 #初始值
# win_point= 0 #初始胜利数
# while count <= 5: #条件表达式
#     if win_point== 3 : #胜利数达到三次
#         print('恭喜你，你成功赢了3场')
#         win_point += 1
#     else:
#         print('你的剩余次数还有',6-count,'次')
#         inp = int(input('【请出拳：0：石头 1：剪刀 2：布】：')) #循环缩进 选中+tab
#         computer = random.randint(0, 2) #范围
#         print('电脑出拳：%d' % computer)
#         if inp > 2:
#             print('ERROR')
#         elif inp == 0 and computer == 1: #多条件
#             win_point +=1
#             print('YOU WIN')
#         elif inp == 1 and computer == 2:
#             win_point += 1
#             print('YOU WIN')
#         elif inp == 2 and computer == 0:
#             win_point += 1
#             print('YOU WIN')
#         elif inp == computer:
#             print('平手')
#         else:
#             print('YOU LOSE')
#             pass
#         count+=1 #变量的自增
# print('游戏结束')
#
# for all in range(1,21):
#     print(all,end=' ')
#     if all>=10:
#         break
times=0
count=3
while times<=3:
    age=int(input('请输入您要猜的年龄...')) # int是因为数字是整形的
    if age==25:
        print('猜对了')
        break # 直接中断循环
        pass
    elif age>25:
        print('猜大了，请再试试')
        pass
    else:
        print('猜小了，请再试试')
        pass
    times+=1
    if times==3:
        choose=input('想不想继续猜呢？Y/N')
        if choose=='Y' or choose=='y':
            times=0
            pass
        elif choose=='N' or choose=='n':
            times=4
            pass
        else:
            print('请输入正确的格式...')
    pass

