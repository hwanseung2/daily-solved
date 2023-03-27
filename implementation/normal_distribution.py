import math

mu = 0
sigma = 1

def f(mu, sigma, x):
    return 1 / (sigma * math.sqrt(2 * math.pi)) * math.exp(-(x - mu)**2 / (2*(sigma**2)))

print(f(mu, sigma, x = 0))