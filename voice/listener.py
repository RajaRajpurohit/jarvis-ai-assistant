import speech_recognition as sr


class Listener:

    def __init__(self):

        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        self.recognizer.energy_threshold = 300
        self.recognizer.pause_threshold = 0.8

    def listen(self):

        try:

            with self.microphone as source:

                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)

                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=7)

            text = self.recognizer.recognize_google(audio)

            print("You said:", text)

            return text.lower()

        except sr.WaitTimeoutError:
            return None

        except sr.UnknownValueError:
            return None

        except sr.RequestError:
            return None