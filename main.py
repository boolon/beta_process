import sys
from draw import plot_bernouli_process
from beta_process import *


if __name__ == "__main__":
    X = associated_bernoulli_process(b0_continuous, 1, 10)
    plot_bernouli_process(X)
    sys.exit(0)
