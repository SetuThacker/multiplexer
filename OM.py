"""
Orthogonal Multiplexing (OM) Signal Demonstration

This module demonstrates orthogonal frequency division multiplexing (OFDM) principles.
Three sinusoidal signals at different frequencies are combined and analyzed to verify
their orthogonality property. The script also performs FFT analysis to show the
frequency components of the multiplexed signal.

Author: GitHub User
Date: 2026
"""

import numpy as np
import matplotlib.pyplot as plt

# Time duration
T = 1
fs = 1000
t = np.linspace(0, T, fs)

# Orthogonal frequencies (well-separated for clear orthogonality)
f1 = 100   # 100 Hz
f2 = 200   # 200 Hz
f3 = 300   # 300 Hz

# Generate sinusoidal signals at orthogonal frequencies
s1 = np.sin(2 * np.pi * f1 * t)
s2 = np.sin(2 * np.pi * f2 * t)
s3 = np.sin(2 * np.pi * f3 * t)

# Combine signals via multiplexing (sum)
s_total = s1 + s2 + s3

# Verify orthogonality using inner product (should be ~0)
dot12 = np.trapezoid(s1 * s2, t)
dot13 = np.trapezoid(s1 * s3, t)
dot23 = np.trapezoid(s2 * s3, t)

print("Orthogonality Check - Inner Products (should be ~0):")
print(f"  s1·s2 = {dot12:.2e}")
print(f"  s1·s3 = {dot13:.2e}")
print(f"  s2·s3 = {dot23:.2e}")
print()

# Plot individual signals and multiplexed signal
plt.figure(figsize=(10, 8))

plt.subplot(4, 1, 1)
plt.plot(t, s1, linewidth=2)
plt.title("Signal 1 (f = 100 Hz)")
plt.ylabel("Amplitude")
plt.grid(True, alpha=0.3)

plt.subplot(4, 1, 2)
plt.plot(t, s2, linewidth=2)
plt.title("Signal 2 (f = 200 Hz)")
plt.ylabel("Amplitude")
plt.grid(True, alpha=0.3)

plt.subplot(4, 1, 3)
plt.plot(t, s3, linewidth=2)
plt.title("Signal 3 (f = 300 Hz)")
plt.ylabel("Amplitude")
plt.grid(True, alpha=0.3)

plt.subplot(4, 1, 4)
plt.plot(t, s_total, linewidth=2, color='red')
plt.title("Orthogonal Multiplexed Signal (Sum of s1, s2, s3)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Perform FFT analysis to show frequency domain representation
S = np.fft.fft(s_total)
freqs = np.fft.fftfreq(len(S), d=1/fs)

# Only positive frequencies for clarity
mask = freqs >= 0
freqs = freqs[mask]
S = np.abs(S[mask])

# Plot frequency spectrum
plt.figure(figsize=(10, 5))
plt.plot(freqs, S, linewidth=2)
plt.title("FFT of Orthogonal Multiplexed Signal")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True, alpha=0.3)
# plt.xlim([0, 500])
plt.tight_layout()
plt.show()


if __name__ == "__main__":
    pass