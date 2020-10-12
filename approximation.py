import numpy as np
import matplotlib.pyplot as plt
from interpolation import func

N = 0 # TODO: replace with real N
I0 = 0 # TODO: replace with real I0
r_beta = 1

def get_approx_func(coeffs):
    def func(t):
        Ht = t # replace with your implementation
        return Ht
    return func

if __name__ == "__main__":
    bound = input("Please input the error bound:")
    approx_func = get_approx_func(float(bound))

    f, (ax1, ax2) = plt.subplots(1, 2)
    t = np.arange(0, 10, 0.1)
    I_approx = approx_func(t)
    I = func(t)

    ax1.plot(t, I)
    ax2.plot(t, I_approx, c='r')
    plt.show()





