# Signal Multiplexing Demonstrations

A Python project demonstrating different signal multiplexing techniques: Time Division Multiplexing (TDM) and Orthogonal Multiplexing (OM).

## Description

This project explores two fundamental multiplexing approaches:

1. **TDM (Time Division Multiplexing)**: Four different signals (sine wave, ramp, cosine, and constant) are sampled sequentially in time slots and combined into a single TDM signal.

2. **OM (Orthogonal Multiplexing)**: Three sinusoidal signals at different frequencies are multiplexed using orthogonal frequency division principles, demonstrating how orthogonal signals can be simultaneously transmitted without interference.

## Features

### TDM Implementation

- Four input signals: sine wave, ramp, cosine wave, and constant signal
- Configurable samples per time slot
- Color-coded visualization of multiplexed signals showing which channel is active at each time

### OM Implementation

- Three orthogonal sinusoidal signals at different frequencies (100 Hz, 200 Hz, 300 Hz)
- Orthogonality verification via inner product calculation
- Time-domain and frequency-domain (FFT) visualization
- Clear separation of frequency components

## Requirements

- Python 3.7+
- NumPy
- Matplotlib

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### TDM Example

```bash
python TDM.py
```

Generates a plot with 5 subplots:

- Signal A: Sine wave (5 Hz)
- Signal B: Ramp signal
- Signal C: Cosine wave (3 Hz)
- Signal D: Constant signal
- TDM Multiplexed Signal: Combined signal with color-coded channels

### OM Example

```bash
python OM.py
```

Generates two plots:

- **Time-domain plot**: Individual signals and their orthogonal sum
- **Frequency-domain plot**: FFT showing the three distinct frequency components

The orthogonality check output shows inner products ≈ 0 (confirming signals are orthogonal)

## Parameters

### TDM

Edit `TDM.py` to adjust:

- `samples_per_slot`: Number of samples per channel in each time slot (default: 5)
- `t`: Time axis range and resolution (default: 0 to 1 second with 1000 points)

### OM

Edit `OM.py` to adjust:

- `f1`, `f2`, `f3`: Frequency of each signal (default: 100 Hz, 200 Hz, 300 Hz)
- `fs`: Sampling frequency (default: 1000 Hz)
- `T`: Time duration (default: 1 second)
- `t`: Time axis range and resolution (default: 0 to 1 second with 1000 points)

## License

MIT License
