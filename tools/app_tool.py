import subprocess
import webbrowser


class AppTool:

    def open_chrome(self):
        subprocess.Popen(
            r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        )
        return "Opening Chrome."

    def open_spotify(self):
        webbrowser.open("https://open.spotify.com/")
        return "Opening Spotify."

    def open_youtube(self):
        webbrowser.open("https://www.youtube.com/")
        return "Opening YouTube."

    def open_github(self):
        webbrowser.open("https://github.com/")
        return "Opening GitHub."

    def play_i_will_survive(self):
        webbrowser.open("https://open.spotify.com/track/5pU2jicRzE4NAgXE7rOcKV?si=413082d1e48640a6")
        return "Playing I Will Survive."