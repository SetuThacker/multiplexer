# TDM Signal Multiplexing

A Python implementation demonstrating Time Division Multiplexing (TDM) of multiple signals.

## Description

This project multiplexes 4 different signals (sine wave, ramp, cosine, and constant) using Time Division Multiplexing techniques. Each signal is sampled in time slots and combined into a single TDM signal, with visualization of both the original signals and the multiplexed output.

## Features

- Four input signals: sine wave, ramp, cosine wave, and constant signal
- TDM multiplexing with configurable samples per slot
- Color-coded visualization of multiplexed signals
- Matplotlib-based plotting

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

Run the script:

```bash
python main.py
```

This will generate a plot with 5 subplots:

- Signal A: Sine wave
- Signal B: Ramp signal
- Signal C: Cosine wave
- Signal D: Constant signal
- TDM Multiplexed Signal: Combined signal with color-coded channels

## Parameters

Edit `main.py` to adjust:

- `samples_per_slot`: Number of samples per channel in each time slot (default: 5)
- `t`: Time axis range and resolution (default: 0 to 1 second with 1000 points)

## License

MIT License
