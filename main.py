import numpy as np

def fft(signal):
    N = len(signal)
    if N <= 1:
        return signal
    even = fft(signal[0::2])
    odd = fft(signal[1::2])
    T = [np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]

# Main program
input_str = input("Masukkan sinyal (pisahkan dengan spasi): ")
input_signal = [complex(num) for num in input_str.split()]
output_signal = fft(input_signal)
print("Hasil transformasi Fourier diskret:")
print(output_signal)