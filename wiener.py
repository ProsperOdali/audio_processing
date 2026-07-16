import numpy as np
import matplotlib.pyplot as plt
import librosa
import soundfile as sf

def wiener_donoise(signal: np.ndarray, sr=None) -> np.ndarray:
    """
    This function tries to produce a desired clean signal
    from a noisy signal
    ------------------
    Parameters:
    signal (np.ndarray): 
    alpha:
    """
    # Get STFT matrix
    signal_sftf_matrix = librosa.stft(signal)

    # Noise estimation
    noise_audio = signal[-2 * sr:]
    noise_stft = librosa.stft(noise_audio)
    noise_power = np.median(np.abs(noise_stft)**2, axis=1)

    # Compute Wiener gain
    noisy_signal_power = np.abs(signal_sftf_matrix) ** 2
    desired_signal_power = np.maximum(
        noisy_signal_power - noise_power[:, None],
        0
    )

    eps = 1e-10
    wiener_gain = desired_signal_power / (noisy_signal_power + eps)

    # Get the desired signal matrix
    desired_signal = signal_sftf_matrix * wiener_gain
    desired_clean_signal = librosa.istft(desired_signal)
    return desired_clean_signal

audio, sr = librosa.load("Coffee Cake (clip) - noise.wav", sr=None)
clean = wiener_donoise(audio, sr)
sf.write("bruh01.wav", clean, sr)