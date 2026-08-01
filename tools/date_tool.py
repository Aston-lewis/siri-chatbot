from datetime import datetime


class DateTool:
    """
    Returns the current system date.
    """

    def execute(self) -> str:

        current_date = datetime.now().strftime("%d %B %Y")

        return f"Today's date is {current_date}."