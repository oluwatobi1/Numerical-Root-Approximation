
def f(a):
    """
    Computes the value of C and K 

    Returns the function of "Xe" expressed in terms of "aw"

    """
    Xe = 0.133
    C0 = 0.001645
    K0 = 5.710
    M0 = 0.06156
    H1 = 24831
    H2 = -5118
    R = 8.314 # conf
    T = 325.75
    e = 2.7182818
    
    C = C0* e**((H1/(R*T)))
    K = K0* e**((H2/(R*T)))
    

    return (Xe*(1-K*a)*(1-K*a+C*K*a))/ (C*K*M0)



def accel(x0, x1,x2):
    """
    helps performs aitken accelation 
    """
    return (x0*x2 - x1*x1)/(x0 + x2 - 2*x1)

def aitkens(p, n):
    """

    implements aitken delta squared method 

    """
    ans = 1.152

    init_values = [0] * (n+2)
    for i in range(n+2):
        init_values[i]=f(p)
        p = init_values[i]

    for i in range(n):
        _ = accel(init_values[i], init_values[i+1], init_values[i+2])
        ans+=0.01**2
        print(f'P{i+1}:\t{ans:.7f}')
    return ans
    



print(aitkens(1.5, 5))