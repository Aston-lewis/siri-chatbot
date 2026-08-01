from datetime import datetime


class TimeTool:
    """
    Returns the current system time.
    """

    def execute(self) -> str:

        current_time = datetime.now().strftime("%I:%M %p")

        return f"The current time is {current_time}."