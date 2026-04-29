"""
Time Division Multiplexing (TDM) Signal Demonstration

This module demonstrates TDM by multiplexing 4 different signals and visualizing
both the original signals and the multiplexed output with color-coded channels.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Time axis - 1 second with 1000 sample points
t = np.linspace(0, 1, 1000)

# Define 4 signals
A = np.sin(2 * np.pi * 5 * t)        # sine wave
B = t                                # ramp
C = np.cos(2 * np.pi * 3 * t)        # cosine
D = np.ones_like(t) * 0.5            # constant

signals = [A, B, C, D]
num_channels = len(signals)

# TDM parameters
samples_per_slot = 5   # how many samples per channel each time
tdm_signal = []
tdm_time = []

index = 0

# Build TDM signal
while index < len(t):
    for ch in range(num_channels):
        if index >= len(t):
            break
        # take small chunk from each signal
        chunk = signals[ch][index:index+samples_per_slot]
        t_chunk = t[index:index+samples_per_slot]

        tdm_signal.extend(chunk)
        tdm_time.extend(t_chunk)

        index += samples_per_slot

tdm_signal = np.array(tdm_signal)
tdm_time = np.array(tdm_time)

# Plot original signals
plt.figure(figsize=(12, 8))

plt.subplot(5,1,1)
plt.plot(t, A)
plt.title("Signal A")

plt.subplot(5,1,2)
plt.plot(t, B)
plt.title("Signal B")

plt.subplot(5,1,3)
plt.plot(t, C)
plt.title("Signal C")

plt.subplot(5,1,4)
plt.plot(t, D)
plt.title("Signal D")

# Plot TDM output
plt.subplot(5,1,5)
plt.plot(tdm_time,tdm_signal, color= "b")
colors = ['red', 'blue', 'green', 'orange']
legend_elements = [Patch(facecolor=colors[i], label=f'Signal {chr(65+i)}') 
                   for i in range(num_channels)]
plt.legend(handles=legend_elements)

index = 0

while index < len(tdm_signal):
    for ch in range(num_channels):
        if index >= len(tdm_signal):
            break
        # Plot each channel's chunk with its own color
        end_index = min(index + samples_per_slot, len(tdm_signal))
        plt.plot(tdm_time[index:end_index], tdm_signal[index:end_index], 
                 color=colors[ch], linewidth=2)
        index = end_index

plt.title("TDM Multiplexed Signal")

plt.tight_layout()
plt.show()