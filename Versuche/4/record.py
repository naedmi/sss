import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


def trigger(array):
    start = next(x for x, val in enumerate(array)
                 if val > 500) - 200
    triggered = array[start:start + SAMPLEFREQ]  # 0 to SAMPLEFREQ is 1 second
    return triggered


if __name__ == "__main__":
    # datetime object containing current date and time
    now = datetime.now()
    dt_string = now.strftime('%Y%m%d_%H%M%S')

    FORMAT = pyaudio.paInt16
    SAMPLEFREQ = 44100
    FRAMESIZE = 1024
    NOFFRAMES = 200
    p = pyaudio.PyAudio()

    print('recording...')
    stream = p.open(input_device_index=1, format=FORMAT, channels=1, rate=SAMPLEFREQ,
                    input=True, frames_per_buffer=FRAMESIZE)
    data = stream.read(NOFFRAMES * FRAMESIZE)
    decoded = np.frombuffer(data, np.int16)
    stream.stop_stream()
    stream.close()
    p.terminate()
    print('done')

    plt.plot(decoded)
    plt.title('without trigger')
    plt.show()

    decoded = trigger(decoded)

    plt.plot(decoded)
    plt.title('with trigger')
    # plt.savefig(f'plots/recording_{dt_string}.png')
    # np.save(f'data/recording_{dt_string}', decoded)
    # plt.savefig(f'plots/recording_tief_5.png')
    np.save(f'data/test/recording_tief_5', decoded)  # .npy file
    plt.show()
