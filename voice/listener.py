from faster_whisper import WhisperModel
import sounddevice as sd
from scipy.io.wavfile import write


class Listener:

    def __init__(self):
        self.model = WhisperModel(
            "base",
            device="cpu",
            compute_type="int8"
        )

    def listen(self, filename="recording.wav", duration=5, sample_rate=16000):

        print("Listening...")

        audio = sd.rec(
            int(duration * sample_rate),
            samplerate=sample_rate,
            channels=1,
            dtype="int16"
        )

        sd.wait()

        write(filename, sample_rate, audio)

        print("Transcribing...")

        segments, _ = self.model.transcribe(filename)

        text = ""

        for segment in segments:
            text += segment.text

        return text.strip()