# if-else 的嵌套使用
score=int(input('请输入你的学分'))
if score>=10:
    grade = int(input('请输入你的成绩'))
    if grade>=70:
        print('恭喜你升班')
        pass
    else:
        print('很遗憾，你留级了哦ww')
        pass
    pass
else:
    print('你太令人失望了')