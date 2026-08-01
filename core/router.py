from core.brain import Brain
from tools.time_tool import TimeTool
from tools.date_tool import DateTool
from tools.system_tool import BatteryTool
from tools.app_tool import AppTool


class Router:

    def __init__(self):
        self.brain = Brain()
        self.time_tool = TimeTool()
        self.date_tool = DateTool()
        self.battery_tool = BatteryTool()
        self.app_tool = AppTool()

    def handle(self, prompt: str, memory) -> str:

        text = prompt.lower().strip()

        text = text.replace(",", "")
        text = text.replace(".", "")    
        text = text.replace("?", "")
        text = text.replace("!", "")

        # Store user message
        memory.add_user(prompt)

        if "time" in text:

            response = self.time_tool.execute()

        elif "date" in text:

            response = self.date_tool.execute()

        elif "battery" in text:

            response = self.battery_tool.execute()

        elif "open chrome" in text:

            response = self.app_tool.open_chrome()

        elif "open spotify" in text:

            response = self.app_tool.open_spotify()

        elif "play" in text and "i will survive" in text:

            response = self.app_tool.play_i_will_survive()

        elif "open youtube" in text:

            response = self.app_tool.open_youtube()

        elif "open github" in text:

            response = self.app_tool.open_github()

        else:

            response = self.brain.think(
                memory.get_messages()
            )

        # Store assistant response
        memory.add_assistant(response)

        return response