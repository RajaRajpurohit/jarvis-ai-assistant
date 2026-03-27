import numpy as np
import logging
from faster_whisper import WhisperModel


class WhisperEngine:

    def __init__(self):

        self.model = WhisperModel(
            "tiny.en",
            device="cpu",
            compute_type="int8",
            cpu_threads=4
        )

        logging.info("Whisper loaded")

    def transcribe(self, audio):

        try:

            audio = np.array(audio).astype(np.float32)

            segments, _ = self.model.transcribe(
                audio,
                beam_size=1,
                best_of=1,
                vad_filter=False,
                temperature=0
            )

            text_parts = []

            for seg in segments:

                t = seg.text.strip().lower()

                if len(t) < 2:
                    continue

                text_parts.append(t)

            text = " ".join(text_parts).strip()

            if len(text.split()) > 8:
                return ""

            return text

        except Exception as e:

            logging.error(f"Whisper error: {e}")
            return ""