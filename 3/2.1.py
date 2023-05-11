import matplotlib.pyplot as plt
import data.measurements as data

if __name__ == '__main__':
    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle('small speaker')
    ax1.plot(data.freq, data.amplitude_small, label='amplitude in mV')
    ax2.plot(data.freq, data.phase_shift_small, label='phase shift in µsec')
    ax1.set(ylabel='amplitude in mV')
    ax2.set(xlabel='frequency in Hz', ylabel='phase shift in µsec')
    ax1.legend()
    ax2.legend()
    plt.savefig('plots/small_speaker.png')
    plt.show()

    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle('big speaker')
    ax1.plot(data.freq, data.amplitude_big, label='amplitude in mV')
    ax2.plot(data.freq, data.phase_shift_big, label='phase shift in µsec')
    ax1.set(ylabel='amplitude in mV')
    ax2.set(xlabel='frequency in Hz', ylabel='phase shift in µsec')
    ax1.legend()
    ax2.legend()
    plt.savefig('plots/big_speaker.png')
    plt.show()
