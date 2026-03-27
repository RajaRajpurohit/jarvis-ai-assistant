import webrtcvad
import numpy as np


class VoiceActivityDetector:

    def __init__(self, sample_rate=16000):

        self.sample_rate = sample_rate
        self.vad = webrtcvad.Vad(2)

        self.frame_duration = 30
        self.frame_size = int(sample_rate * self.frame_duration / 1000)

    # =============================
    # GENERATE FRAMES
    # =============================

    def frame_generator(self, audio):

        n = self.frame_size

        for i in range(0, len(audio), n):

            frame = audio[i:i+n]

            if len(frame) < n:
                continue

            frame_int16 = (frame * 32768).astype(np.int16)

            yield frame_int16.tobytes()

    # =============================
    # CHECK SPEECH
    # =============================

    def is_speech(self, frame):

        return self.vad.is_speech(frame, self.sample_rate)