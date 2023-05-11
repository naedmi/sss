import redlab as rl
import matplotlib.pyplot as plt

# Abtastfrequenz 8000

while True:
    messreihe = rl.cbVInScan(0, 0, 0, 500, 8000, 1)
    plt.plot(messreihe)
    plt.show()
