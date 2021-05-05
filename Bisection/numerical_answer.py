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
    #Evaluate C and K
    C = C0* e**((H1/(R*T)))
    K = K0* e**((H2/(R*T)))
    #Evaluate the Xe
    return (C*K*a*M0)/((1-K*a)*(1-K*a+C*K*a))




def bisection(lower_bound, upper_bound, iterations=10):    
    '''
    Takes a lower bound, upper bound and number of iteration

    Returns the roots.    
    '''

    
    if f(lower_bound)*f(upper_bound)>=0:
        print("No root in range")

    lower=lower_bound
    upper=upper_bound

    # carrys out bisection for specified iteration
    for i in range(1, iterations+1):
        mid = (lower+upper)/2
        f_mid = round(f(mid),3)
        print(mid)

        
        if f(lower)*f_mid<0:
            lower=lower
            upper =mid

        elif f(upper)*f_mid<0:
            lower=mid
            upper=upper
        elif f_mid == 0:
            print("The exact solution is ", mid)
            return mid
        else:
            print("No root in range")
    return (mid)


print(bisection(lower_bound = 0, upper_bound = 2))