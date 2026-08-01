import psutil


class BatteryTool:
    """
    Returns the laptop battery percentage.
    """

    def execute(self) -> str:

        battery = psutil.sensors_battery()

        if battery is None:
            return "Battery information is unavailable."

        percent = battery.percent

        if battery.power_plugged:
            return f"Battery is {percent}% and currently charging."

        return f"Battery is {percent}%."