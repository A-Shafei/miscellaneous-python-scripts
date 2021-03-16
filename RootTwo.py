import numpy as np
import matplotlib.pyplot as plt

def main():
    
    def f(y):
        return y
    
    k1 = None
    k2 = None
    k3 = None
    k4 = None

    dx = 0.000000001

    y = 1

    for x in np.arange(0, 1+dx, dx):
        
        k1 = (y)
        k2 = (y + dx * k1 / 2)
        k3 = (y + dx * k2 / 2)
        k4 = (y + dx * k3)

        y = y + (1/6) * dx * (k1 + 2*k2 + 2*k3 + k4)

    print(y)


main()
