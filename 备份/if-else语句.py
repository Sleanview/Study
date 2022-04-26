# 同时多条备注 Crtl+/

# 单分支
# if 条件表达式：
#    代码指令
#    ......

# score=80
# if score<=60: #满足条件就会输出打印的值
#     print('成绩不合格')
#     pass #空语句
#
# print('语句运行结束')

# 双分支
# if 条件表达式：
#    代码指令
# else:
#    代码指令

# score=50
# if score>60: #Ture
#     print('成绩合格')
#     pass
# else: #False时候才会执行
#     print('成绩不合格')
#     pass

# 多分支的选择【多个条件】
# if 条件表达式：
#    代码指令
# elif 条件表达式:
#    代码指令
# ......
#   else:
# 特征：
# 1.只要满足其中一个分支，就会推出本层if语句结构【必定会执行其中一个分支】
# 2.至少有两种情况可以选择
# elif 后面必须写上条件和语句
# elif 是选配，根据实际情况来写

# score=int(input('请输入你的成绩：'))
# if score>=90:
#     print('优秀')
#     pass
# elif score>=80:
#     print('良好')
#     pass
# elif score>=60:
#     print('及格')
#     pass
# else:
#     print('速速回家种地')

#猜拳击小游戏
# 0：石头 1：剪刀 2：布
import random #直接导入，产生随机数的模块
#计算机 人
inp = int(input('请出拳：【0：石头 1：剪刀 2：布】：'))
computer = random.randint(0, 2)
print('电脑出拳：%d' % computer)
if inp > 2:
    print('输入错误')
elif inp == 0 and computer == 1:
    print('YOU WIN!')
elif inp == 1 and computer == 2:
    print('YOU WIN!')
elif inp == 2 and computer == 0:
    print('YOU WIN!')
elif inp == computer:
    print('平手')
else:
    print('YOU LOSE...')
