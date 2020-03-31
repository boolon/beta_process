import matplotlib.pyplot as plt
import matplotlib.lines as mlines

def plot_bernouli_process(X, c, gamma):
    """
    X should correspond to the X1...n
    """
    n = len(X)
    for i in range(n):
        for el in X[i]:
            plt.plot([el, el],[i, i+1], "k")
            plt.title("Beta process for {} samples (c = {},γ = {})".format(n, c, gamma))
    plt.show()
