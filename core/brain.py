import ollama


class Brain:
    """
    Responsible for communicating with the local AI model.
    """

    def __init__(self):
        self.model = "llama3.2:latest"

    def think(self, messages) -> str:

        try:

            response = ollama.chat(
                model=self.model,
                messages=messages,
            )

            return response["message"]["content"]

        except Exception as error:

            return f"Error: {error}"