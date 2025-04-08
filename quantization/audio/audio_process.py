import numpy as np
import matplotlib.pyplot as plt
import librosa # signal is mp3

file_path = '/home/albu/Documents/masters/pds/signal-processing-scripts/quantization/audio/speech.mp3'
signal, sample_rate = librosa.load(file_path, sr=None)

#signal = signal / np.max(np.abs(signal))

fft_result = np.fft.fft(signal)
magnitude_spectrum = np.abs(fft_result)  
frequencies = np.fft.fftfreq(len(signal), d=1/sample_rate)

'''
Plotting the magnitude in the spectrum 
The max frequency is higher than 4K, because its not my voice.
I took this video from youtube x.x
'''
positive_freqs = frequencies[:len(frequencies)//2]
positive_magnitude = magnitude_spectrum[:len(magnitude_spectrum)//2]

num_bins = 150  
hist, bin_edges = np.histogram(positive_freqs, bins=num_bins, weights=positive_magnitude, density=True)

# Plot the histogram
plt.figure(figsize=(10, 6))
plt.bar(bin_edges[:-1], hist, width=np.diff(bin_edges), align='edge', alpha=1)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Probability Density')
plt.grid(axis='y', linestyle=':', linewidth=0.7)
plt.show()

'''
A uniform quantizer ensures that the level height is constant across the entire range of the signal.
I.e., the quantization levels are evenly spaced, whe \delta=cte. This makes the quantization process simple and efficient
for uniformly distributed signals. However, for speaker signals, the quantization levels are not evenly spaced, because 
people speak at different frequencies and amplitudes. This means that the quantization levels are not evenly spaced,
which can lead to distortion, loss of information and inefficient bit allocation.
'''

signal_power = np.mean(signal**2)
quantized_signal = np.round(signal)  # Uniform quantization, assuming a \delta of 1
quantization_error = signal - quantized_signal
quantization_error_power = np.mean(quantization_error**2)

# Compute the quantization SNR (SNRq)
signal_power_db = 10 * np.log10(signal_power)
quantization_error_power_db = 10 * np.log10(quantization_error_power)
# SNRq in dB
SNRq = signal_power_db - quantization_error_power_db

# Print the result
print(f"Signal Power: {signal_power} dB")
print(f"Quantization Error Power: {quantization_error_power} dB")
print(f"SNRq (Quantization SNR): {SNRq} dB")