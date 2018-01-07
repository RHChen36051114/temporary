import sys
import math as m
import random as r
import matplotlib.pyplot as plt
import numpy as np


def gen_NormalRV () :

    # use "Rejection Method"
    #    f(Y)
    #  -------  >= U,  Y = expoRV,  U = uniformRV
    #   c*g(Y)

    #  f(x) = normal distribution PDF function
    #  g(x) = exponential distribution PDF

    # generate uniform RV
    U = r.random()

    # generate expoential RV
    Y = -m.log(r.random())

    if m.exp((-(Y-1)**2)/2) >= U :
        return Y
    else :
        return gen_NormalRV()


def test_NRV () :

    y_his = []

    # normal RV from Reject Method
    '''
    for cnt in range(1000) :
        y_his.append (gen_NormalRV())
    '''

    # normal RV from numpy lib
    mu, sigma = 0, 1
    y_his = np.random.normal (mu, sigma, 10000)

    plt.hist (y_his)
    plt.show()


def expo_draw () :

    '''
    x = np.linspace(0,4,1000)
    y_exp = np.exp(x)
    y_squ = x**2
    '''
    x = np.linspace (0, 1, 1000)
    y = np.exp ((-(x-1)**2)/2)

    '''
    plt.plot (x, y_exp)
    plt.plot (x, y_squ)
    '''
    plt.plot (x, y)
    plt.show()


def sample_mean (lis) :
    return np.mean(lis)


def sample_std (lis) :
    return np.std(lis)


def main (threshold) :

    boundary = 0
    thr = []
    lis = []

    for counter in range(1) :
        for cnt in range(100000) :
            lis.append (np.random.normal(0, 1, 1))
            print (np.mean(lis))
            print (sample_std(lis))
            print (sample_std(lis)/((cnt+1)**0.5))
            if sample_std(lis)/((cnt+1)**0.5) < threshold :
                boundary = cnt+1
                if boundary > 10 :
                    thr.append (boundary)
                    boundary = 0
                    break
            print ('----------')
        print ("\n<0.1 need times  :  %d" % (cnt+1))
    #print ("Average threshold times  :  %f" % np.mean(thr))

    '''
    plt.hist (np.random.normal(0, 1, 1000))
    plt.show()
    '''

if __name__ == "__main__" :

    main(float(sys.argv[1]))

