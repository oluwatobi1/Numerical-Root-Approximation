Xe = 0.133
C0 = 0.001645
K0 = 5.710
M0 = 0.06156
H1 = 24831
H2 = -5118
R = 8.314 # conf
T = 325.75
e = 2.7182818

# Evaluate C and K
C = C0* e**((H1/(R*T)))
K = K0* e**((H2/(R*T)))

def f(x):  
    """
    Returns the function of "Xe" expressed in terms of "aw"
    """  
    try:
        return (C*K*x*M0)/((1-K*x)*(1-K*x+C*K*x))
    except ZeroDivisionError as e:
        return 0

def g(x):
    """
    Returns the differential of "Xe" expressed in terms of "x"
    """ 
    return (C*K*M0)*(1-(K*x**2*(K+C*K))) / ((1-K*x)*(1-K*x+C*K*x))**2

def newton_raphson(x0, e=0.00001, total_iterations=15):
    """
    Takes in an initial root, error_threshold value, and maximum number of iteration
    
    carrys out newton raphson method to find approximate root
    """
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
            print("Newton Raphson Mtd: next root at  ", x1)           
        else:
            print(" Not convergent")
    return x1

print(newton_raphson(x0=2))
