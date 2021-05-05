def f(x):
    return (x**2)-2

def g(x):
    return 2*x

def newton_raphson(x0, e=0.00001, total_iterations=15):
    steps_taken = 0
    checker = 1
    condition = True

    while condition:
        if g(x0) == 0.0:            
            print("Zero division")
            break

        x1 = x0 - f(x0)/g(x0)
        x0=x1
        steps_taken+=1

        if steps_taken > total_iterations:
            checker = 0
            break
        
        condition = abs(f(x1)) > e
        # print(x1, condition, 'iterations: ', steps_taken)

        if checker==1:
            print("next root at  ", x1)           
        else:
            print(" Not convergent")
    return x1
# Testing here
print(newton_raphson(x0=2))
