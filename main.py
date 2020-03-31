import sys, getopt
from draw import plot_bernouli_process
from beta_process import *


def main(argv):
    try:
        opts, args = getopt.getopt(argv,"c:g:n:",["gamma="])
    except getopt.GetoptError:
        sys.exit(2)

    c = 1
    gamma = 10
    n = 20
    for opt, arg in opts:
        if opt in ("-c"):
            c = float(arg)
        elif opt in ("-n"):
            n = int(arg)
        elif opt in ("-g","--gamma"):
            gamma = float(arg)

    X = associated_bernoulli_process(b0_continuous, c, gamma, n = n)
    plot_bernouli_process(X, c, gamma)

if __name__ == "__main__":
    main(sys.argv[1:])
    sys.exit(0)
