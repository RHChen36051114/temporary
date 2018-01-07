import sys
import random as r
import numpy as np


def gen_random_exceed_1 (times) :
    l = []

    for cnt in range(times) :
        rv = 0
        count = 0
        while rv < 1 :
            rv += r.random()
            count += 1
        l.append (count)

    return l


def main (times) :
    lis = gen_random_exceed_1 (times)
    avg = np.mean (lis, dtype=np.float64)
    print ("Avg  :  ", avg)
    print ("Var  :  ", np.var(lis))

    # 95% CI lay in +- 1.96 Std
    boundary = 1.96 * (np.std(lis)/times**0.5)
    print ("Confindece Interval(95%)  :  ", "%f +- %f" % (avg, boundary))
    print (avg-boundary, "\t~\t", avg+boundary)


if __name__ == "__main__" :
    main (int(sys.argv[1]))

