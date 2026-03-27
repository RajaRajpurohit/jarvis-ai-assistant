import json
import logging
import google.generativeai as genai


class AIEngine:

    def __init__(self, memory_engine=None):

        self.memory = memory_engine
        self.model = None

        try:

            with open("secrets.json", "r") as f:
                secrets = json.load(f)

            api_key = secrets.get("GEMINI_API_KEY")

            if not api_key:
                logging.error("Gemini API key not found in secrets.json")
                return

            genai.configure(api_key=api_key)

            self.model = genai.GenerativeModel("gemini-1.5-flash")

            logging.info("Gemini AI Engine initialized")

        except Exception as e:

            logging.error(f"AI Engine init error: {e}")

    # ==================================
    # ASK GEMINI
    # ==================================

    def ask(self, prompt, context=None):

        if not self.model:
            return None

        try:

            full_prompt = prompt

            if context:

                history = context.get_history()

                if history:

                    conversation = ""

                    for item in history[-5:]:

                        conversation += f"User: {item['command']}\n"
                        conversation += f"Jarvis: {item['response']}\n"

                    full_prompt = conversation + f"\nUser: {prompt}\nJarvis:"

            response = self.model.generate_content(full_prompt)

            if not response or not response.text:
                return None

            answer = response.text.strip()

            if self.memory:
                self.memory.remember(prompt, answer)

            return answer

        except Exception as e:

            logging.error(f"Gemini error: {e}")

            return None    