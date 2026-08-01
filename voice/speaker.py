from email.mime import audio
from pathlib import Path
import subprocess
import tempfile
import os
import sounddevice as sd
from scipy.io.wavfile import read


class Speaker:

    def __init__(self):

        base_dir = Path(__file__).resolve().parent.parent

        self.piper = base_dir / "piper" / "piper.exe"
        self.model = base_dir / "piper" / "en_US-lessac-medium.onnx"

    def speak(self, text: str):

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".wav"
        ) as temp_file:

            output_file = temp_file.name

        subprocess.run(
            [
                str(self.piper),
                "-m",
                str(self.model),
                "-f",
                output_file
            ],
            input=text,
            text=True,
            check=True
        )

        

        sample_rate, audio = read(output_file)

        sd.play(audio, sample_rate)
        sd.wait()

        os.remove(output_file)