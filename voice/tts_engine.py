import asyncio
import edge_tts
import tempfile
import playsound
import threading


class TextToSpeech:

    def __init__(self):
        self.voice = "en-US-GuyNeural"
        self.is_speaking = False
        self.thread = None

    async def speak_async(self, text):

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            filename = fp.name

        communicate = edge_tts.Communicate(text, self.voice)

        await communicate.save(filename)

        playsound.playsound(filename)

    def _run(self, text):

        try:
            self.is_speaking = True
            asyncio.run(self.speak_async(text))
        except Exception as e:
            print("TTS Error:", e)
        finally:
            self.is_speaking = False

    def speak(self, text):

        if not text:
            return

        if self.is_speaking:
            return

        self.thread = threading.Thread(target=self._run, args=(text,))
        self.thread.start()

    def stop(self):

        # stops future speech
        self.is_speaking = False