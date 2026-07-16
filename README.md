# Audio Processing: Classical Audio Denoising in Python

## Overview

This project explores classical digital signal processing (DSP) techniques for reducing background noise in audio recordings using Python.

Rather than relying on deep learning models, the repository implements traditional denoising algorithms based on spectral analysis and statistical signal estimation. The goal is to understand how these methods work and evaluate their strengths and limitations on real audio recordings.

Currently implemented algorithms include:

- Spectral Gating
- Frequency-Domain Wiener Filtering

---

## Features

- Load WAV audio files
- Compute the Short-Time Fourier Transform (STFT)
- Estimate background noise from:
  - A known noise-only segment of the recording, or
  - Low-energy frames (experimental)
- Apply spectral gating
- Apply Wiener filtering
- Reconstruct the enhanced signal using the inverse STFT
- Save the denoised audio

---

## Repository Structure

```
audio_processing/
│
├── main.py
├── spectral_gating.py
├── wiener_filter.py
├── requirements.txt
├── README.md
│
├── input/
│   └── noisy.wav
│
├── output/
│   └── denoised.wav
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/audio_processing.git
```

Install the dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

Place a noisy WAV file inside the `input` directory.

Run

```bash
python main.py
```

The denoised audio will be written to the `output` directory.

---

## Implemented Algorithms

### Spectral Gating

Spectral gating estimates the background noise spectrum and attenuates frequency components whose magnitudes are close to the estimated noise floor.

This method is simple and computationally efficient but may introduce musical noise when the noise estimate is inaccurate.

---

### Wiener Filtering

The Wiener filter estimates the clean signal by computing a frequency-dependent gain from estimates of the noisy signal power and the background noise power.

In this implementation, the noise power spectrum can be estimated from:

- a known noise-only section of the recording, or
- automatically selected low-energy frames.

The quality of the denoised audio depends strongly on the quality of the noise estimate.

---

## Project Notes

During development, different noise estimation strategies were compared.

Using a known noise-only segment generally produced better results than estimating noise solely from the lowest-energy frames, highlighting the importance of accurate noise estimation in classical speech enhancement algorithms.

---

## Current Limitations

- Assumes approximately stationary background noise.
- Noise estimation is relatively simple.
- Performance decreases for rapidly changing or highly non-stationary noise.
- Some residual noise or musical artifacts may remain after enhancement.

---

## Future Improvements

Potential extensions include:

- Automatic silence detection
- Voice Activity Detection (VAD)
- Adaptive noise estimation
- MMSE speech enhancement
- Ephraim–Malah filtering
- Deep learning-based speech enhancement

---

## Technologies

- Python
- NumPy
- SciPy
- Librosa
- SoundFile

---

## License

This project is released under the MIT License.