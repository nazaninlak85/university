import numpy as np
import matplotlib.pyplot as plt

def plot_normal_dist(n, mean=0, std=1, bins=70):
    data = np.random.normal(size=n)
    plt.figure(figsize=(8,5))
    plt.hist(data, bins=bins)
    plt.title(f'Normal Distribution(n={n}, mean={mean}, std={std})')
    plt.xlabel('value')
    plt.ylabel('frequency')
    plt.grid(True)
    plt.show()
    
plot_normal_dist(10)
plot_normal_dist(1000)
plot_normal_dist(100_000)