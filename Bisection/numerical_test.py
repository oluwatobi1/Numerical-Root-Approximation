import math

def f(x):
    return (x**2)-2


point = 1
print('Hello there')
b=1+0.1
f1 = f(point)
f2 = f(b)

while f(point)!=0.0:
    print("sent ", f(point))
    print(f1, f2, point)

    if f1*f2<0:
        point = (point+point-0.01)/2
        print(f1, f2, point, f(point))
        if f(point)*f1<0:
            f1 = f(point)
            print(f1, f(point), " f1 point")            
        elif f(point)*f2:
            f2 = f(point)

    else:
        point += 0.01
        f1 = f(point)
        f2 = f(point+0.01)
        print( "next")

    