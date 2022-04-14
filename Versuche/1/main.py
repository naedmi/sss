import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# distance values
x = [10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64, 67, 70]

# mean values of voltage (protocol)
y = [1.362, 1.193, 1.011, 0.9611, 0.8398, 0.8209, 0.7439, 0.6581, 0.618, 0.580, 0.5417, 0.5226,
     0.4473, 0.4474, 0.403, 0.403, 0.3817, 0.3398, 0.300, 0.320, 0.3002]


def conv(_):
    return _.replace(',', '.').encode()


def read(path):
    return np.genfromtxt((conv(_) for _ in open(path)), delimiter=';',
                         dtype=np.double, skip_header=300, skip_footer=50, usecols=1)  # how many entries?


if __name__ == '__main__':
    # read data
    z = []
    std = []
    for num in range(10, 73, 3):
        values = read("data/" + str(num) + ".csv")
        z.append(np.mean(values))
        std.append(np.std(values))

    # calculate logarithms
    logx = list(map(lambda val: np.log(val), x))
    logy = list(map(lambda val: np.log(val), y))

    # calculate linear regression
    result = stats.linregress(logx, logy)
    x1 = np.linspace(np.min(logx), np.max(logx), 21)
    y1 = result.slope * x1 + result.intercept  # slope -> gradient

    # 1st plot - characteristic curve
    plt.title('Kennlinie')
    plt.xlabel('Abstand [cm]')
    plt.ylabel('Spannung [V]')
    plt.plot(x, y, label="protocol", linewidth=1)
    plt.plot(x, z, label="data", linewidth=1)
    plt.legend()
    plt.savefig('plots/characteristic.png')
    plt.show()

    # 2nd plot - standard deviation
    plt.title('Standardabweichung')
    plt.xlabel('Abstand [cm]')
    plt.ylabel('Spannung [V]')
    plt.plot(x, std)
    plt.axis([7, 73, 0, 0.1])
    plt.savefig('plots/std.png')
    plt.show()

    # 3rd plot - logarithm
    plt.title('Logarithmierte Werte')
    plt.xlabel('(logarithmierter) Abstand [cm]')
    plt.ylabel('(logarithmierte) Spannung [V]')
    plt.plot(logx, logy)
    plt.savefig('plots/log.png')
    plt.show()

    # 4th plot - linear regression
    plt.title('Lineare Regression - Ausgleichsgerade')
    plt.xlabel('(logarithmierter) Abstand [cm]')
    plt.ylabel('(logarithmierte) Spannung [V]')
    plt.plot(logx, logy, 'ob')
    plt.plot(x1, y1, '-r')
    plt.savefig('plots/linear-regression.png')
    plt.show()


