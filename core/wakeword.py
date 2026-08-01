import numpy as np
import sounddevice as sd
from openwakeword.model import Model


class WakeWord:
    def __init__(self):
        print("Loading wake word model...")
        self.model = Model(inference_framework="onnx")
        print("Wake word model loaded successfully.")

    def start(self):
        print("Waiting for wake word...")

        sample_rate = 16000
        chunk_size = 1280  # 80 ms of audio

        with sd.InputStream(
            samplerate=sample_rate,
            channels=1,
            dtype="int16",
            blocksize=chunk_size,
        ) as stream:

            while True:
                audio, _ = stream.read(chunk_size)

                audio = audio.flatten().astype(np.int16)


                

            
                prediction = self.model.predict(audio)

                score = float(prediction["hey_jarvis"])

                if score > 0.5:
                    print("🎉 Wake word detected!")
                    break