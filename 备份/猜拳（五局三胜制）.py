#猜拳击小游戏(改-五局三胜制)
# 0：石头 1：剪刀 2：布
import random #直接导入，产生随机数的模块
#计算机 人
count= 1 #初始值
win_point= 0 #初始胜利数
while count <= 5: #条件表达式
    if win_point== 3 : #胜利数达到三次
        print('恭喜你，你成功赢了3场')
        break
    else:
        print('你的剩余次数还有',6-count,'次')
        inp = int(input('【请出拳：0：石头 1：剪刀 2：布】：')) #循环缩进 选中+tab
        computer = random.randint(0, 2) #范围
        print('电脑出拳：%d' % computer)
        if inp > 2:
            print('ERROR')
        elif inp == 0 and computer == 1: #多条件
            win_point +=1
            print('YOU WIN')
        elif inp == 1 and computer == 2:
            win_point += 1
            print('YOU WIN')
        elif inp == 2 and computer == 0:
            win_point += 1
            print('YOU WIN')
        elif inp == computer:
            print('平手')
        else:
            print('YOU LOSE')
            pass
        count+=1 #变量的自增
        if win_point == 3:  # 胜利数达到三次
            print('恭喜你，你成功赢了3场')
            break
print('游戏结束')