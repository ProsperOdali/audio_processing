import librosa
import numpy as np
import soundfile as sf

def denoise(audio_filename: str,
             method: str="hard",
             noise_fraction: float=0.1)-> np.ndarray:
    
    # Load audio
    data, sr = librosa.load(audio_filename, sr=None)

    # Covert to STFT
    stft_matrix = librosa.stft(data)

    # Estimate noise
    frame_energy = np.sum(np.abs(stft_matrix)**2, axis=0)
    num_frames = len(frame_energy)
    num_quiet = int(noise_fraction * num_frames)
    quiet_frames = np.argsort(frame_energy)[:num_quiet]
    quiet_stft = stft_matrix[:, quiet_frames]
    noise_profile = np.median(np.abs(quiet_stft), axis=1)

    if method == "hard":
        # Build mask
        threshold_factor = 2.0
        threshold = threshold_factor * noise_profile[:, None]
        mask = np.abs(stft_matrix) > threshold

        # Apply mask
        stft_filtered = stft_matrix * mask

        # Inverse STFT
        clean = librosa.istft(stft_filtered)

        return clean, sr
    
    elif method == "soft":
        # Compute magnitude
        magnitude = np.abs(stft_matrix)

        #Build the soft gating
        lower_ratio = 1.0
        upper_ratio = 5.0
        epsilon = 1e-10
        ratio = magnitude / (noise_profile[:, None] + epsilon)
        normalized = (ratio - lower_ratio) / (upper_ratio - lower_ratio)
        gain = np.clip(normalized, 0, 1)

        # Apply soft gating
        stft_filtered = stft_matrix * gain

        # Inverse STFT
        clean = librosa.istft(stft_filtered)
        
        return clean, sr