import numpy as np
import sounddevice as sd

sample_rate = 16000
chunk_size = 1280

print("Speak into the microphone...")

with sd.InputStream(
    samplerate=sample_rate,
    channels=1,
    dtype="int16",
    blocksize=chunk_size,
) as stream:

    while True:
        audio, _ = stream.read(chunk_size)
        audio = audio.flatten()

        volume = np.abs(audio).mean()

        print(f"Volume: {volume:.2f}")