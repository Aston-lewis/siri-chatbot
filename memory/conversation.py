class ConversationMemory:
    def __init__(self, max_messages=12):
        self.max_messages = max_messages

        self.messages = [
            {
                "role": "system",
                "content": (
                    "You are Siri, a helpful local AI voice assistant. "
                    "Keep your answers short and natural."
                )
            }
        ]

    def add_user(self, text):
        self.messages.append(
            {
                "role": "user",
                "content": text
            }
        )
        self.trim()

    def add_assistant(self, text):
        self.messages.append(
            {
                "role": "assistant",
                "content": text
            }
        )
        self.trim()

    def get_messages(self):
        return self.messages

    def trim(self):
        system = self.messages[0]
        history = self.messages[1:]

        if len(history) > self.max_messages:
            history = history[-self.max_messages:]

        self.messages = [system] + history

    def clear(self):
        self.messages = [self.messages[0]]