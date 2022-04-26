import math
x=eval(input('输入x:'))
if x>5:
    y=math.sin(x)+(x**2+1)**(1/2)
    print(y)
elif 0<x<=5:
    y=math.e**x + math.log(x,5)+x**(1/5)
    print(y)
else:
    y=math.cos(x)-x**3+3*x
    print(y)