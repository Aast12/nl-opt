import numpy as np
import matplotlib.pyplot as plt


DOMAIN_LB = 0
DOMAIN_UB = 2
N = 250


def f(X):
    return np.exp(-3 * X) * np.sin(20 * X)


def g(X):
    return [x ** (1 / 4) if x <= 1 else 1 for x in X]


def ex5_1():
    domain = np.linspace(DOMAIN_LB, DOMAIN_UB, N)

    plt.plot(domain, f(domain), label="f(x) = exp(-3x) * sin(20x)")
    plt.plot(domain, g(domain), label="g(x) = x^(1/4) if x <= 1 else 1")

    plt.show()


def ex5_2(domain_lb: float, domain_ub: float, n: float = 250):
    f = lambda x, y: np.sin(x + y) * np.sin(x - y)
    domain = np.linspace(domain_lb, domain_ub, n)

    (
        xv,
        yv,
    ) = np.meshgrid(domain, domain)
    z = f(xv, yv)

    ax = plt.figure().add_subplot(projection="3d")
    ax.plot_surface(xv, yv, z, cmap="viridis")


if __name__ == "__main__":
    # ex5_1()
    ex5_2(-2 * np.pi, 2 * np.pi)
    plt.show()
