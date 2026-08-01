from core.wakeword import WakeWord
from core.router import Router
from voice.listener import Listener
from voice.speaker import Speaker
from memory.conversation import ConversationMemory


def main():
    wakeword = WakeWord()
    listener = Listener()
    router = Router()
    speaker = Speaker()
    memory = ConversationMemory()

    print("Assistant started.")
    speaker.speak("Siri is ready.")

    while True:

        wakeword.start()

        text = listener.listen()

        if not text:
            continue

        print(f"You: {text}")

        response = router.handle(text, memory)

        print(f"Siri: {response}")

        speaker.speak(response)


if __name__ == "__main__":
    main()