import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def load_data(data_path):
    df = pd.read_csv(data_path)
    t = df['t'].values
    I = df['I'].values
    return t, I

def solve(t, I, r_beta):
    # calculation N and I0
    N, I0 = 0, 0  # TODO: use least square method
    return N, I0

if __name__ == "__main__":
    # known parameters
    r_beta = 1

    # load data
    t, I = load_data('data.csv')
    # solve for unknown parameters
    N, I0 = solve(t, I, r_beta)
    print(N, I0)