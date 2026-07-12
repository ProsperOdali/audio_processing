import numpy as np
import matplotlib.pyplot as plt
import librosa
import soundfile as sf

filename = "Coffee Cake (clip).wav"

# Load audio
data, sr = librosa.load(filename, sr=None)

# Add noise to data
eps = 0.07
data += np.random.normal(scale=eps, size=len(data))

# Write the transformed data to disk
sf.write("Coffee Cake (clip) - noised.wav", data, sr)

# View the spectrogram
D = librosa.stft(data)
plt.figure(figsize=(10, 8))
librosa.display.specshow(librosa.amplitude_to_db(np.abs(D), ref=np.max),
                         sr=sr,
                         x_axis='time',
                         y_axis='hz')
plt.colorbar(label='dB')
plt.title('Spectrogram')
plt.show()

frame_energy = np.sum(np.abs(D)**2, axis=0)
plt.figure(figsize=(10, 3))
plt.plot(frame_energy)
plt.xlabel("Frame")
plt.ylabel("Energy")
plt.title("Energy of each STFT frame")
plt.show()


noise_percent = 0.4
num_frames = len(frame_energy)
num_quiet = int(noise_percent * num_frames)
quiet_frames = np.argsort(frame_energy)[:num_quiet]
quiet_stft = D[:, quiet_frames]
noise_profile = np.median(np.abs(quiet_stft), axis=1)

mask = np.abs(D) > 2 * noise_profile[:, None]
D_filtered = D * mask

denoised = librosa.istft(D_filtered)
import soundfile as sf
sf.write("denoised.wav", denoised, sr)