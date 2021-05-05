def accel(x0, x1,x2):
   return (x0*x2 - x1*x1)/(x0 + x2 - 2*x1)

def aitkens(f, p, n):
    init_values = [0] * (n+2)
    for i in range(n+2):
        init_values[i]=f(p)
        p = init_values[i]
    print(init_values)

    for i in range(n):
        result = accel(init_values[i], init_values[i+1], init_values[i+2])
        print(f'P{i+1}:\t{result:.7f}')

import math

f = lambda x: math.exp(-x)

print(aitkens(f, 0.5, 5))