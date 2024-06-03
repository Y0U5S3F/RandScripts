import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from pydub import AudioSegment

# Step 1: Convert MP3 to WAV
audio = AudioSegment.from_mp3("p.mp3")
audio.export("p.wav", format="wav")

# Step 2: Load the audio file
sample_rate, audio_data = wav.read("p.wav")

# Step 3: Apply the Fourier Transform
fft_output = np.fft.fft(audio_data)

# Step 4: Identify Peaks
magnitude_spectrum = np.abs(fft_output)
frequencies = np.fft.fftfreq(len(magnitude_spectrum), 1/sample_rate)
plt.plot(frequencies[:len(frequencies)//2], magnitude_spectrum[:len(frequencies)//2])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Magnitude Spectrum')
plt.show()

# Step 5: Note Identification
# Find peaks in the magnitude spectrum
peaks, _ = find_peaks(magnitude_spectrum[:len(frequencies)//2], height=10000)  # Adjust height threshold as needed

# Map peaks to corresponding notes (you need to have a mapping of piano key frequencies)
piano_key_frequencies = [27.5 * (2 ** (i/12)) for i in range(88)]  # Frequency of each piano key
notes = ['A0', 'A#0/Bb0', 'B0', 'C1', ...]  # Corresponding notes
detected_notes = []
for peak in peaks:
    frequency = frequencies[peak]
    closest_key_index = np.argmin(np.abs(np.array(piano_key_frequencies) - frequency))
    detected_notes.append(notes[closest_key_index])

print("Detected notes:", detected_notes)

# Step 6: Separation (Optional)
# Depending on the frequencies detected, you can choose to separate the notes by filtering the signal.

# Step 7: Post-processing (Optional)
# Refine the separated notes if necessary.