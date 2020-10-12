import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

N = 0 # TODO: replace with real N
I0 = 0 # TODO: replace with real I0
r_beta = 1

def load_table():
    df = pd.read_csv('LUT.csv')
    t = df['t'].values
    I = df['I'].values
    return t, I

def get_hermite_func(t, I):
    # t, I: given t_k and I(t_k)
    def hermite_func(x):
        Ix = x # TODO: replace with hermite interpolation
        return Ix
    return hermite_func

def func(t):
    # calculate I(t)
    It = t # TODO: replace with the real I(t)
    return It


if __name__ == "__main__":
    tk, I_tk = load_table()
    t = np.arange(0, 15, 0.1)

    hermite_func = get_hermite_func(tk, I_tk)

    # calculate
    I = func(t)
    I_hat = hermite_func(t)

    print(np.abs(I_hat - I).max())