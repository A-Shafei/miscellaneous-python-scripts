import math
import matplotlib.pyplot as plt
import numpy as np

def main():
    m = 5
    g = 9.8
    mu = 0.01
    k = 2

    dt = 0.001
    x = 10
    x_1p = 0
    x_2p = None

    first_5k = []

    for i in range(0,3*60*1000):
        first_5k.append(x)
        if x_1p == 0:
            x_2p = (-k/m)*x
        else:
            x_2p = (-k/m)*x - mu*g*(x_1p/math.sqrt((x_1p)**2))
        x = x + x_1p * dt
        x_1p = x_1p + x_2p * dt

    plt.plot(np.arange(0,3*60,0.001), first_5k)
    plt.show()

        
main()
