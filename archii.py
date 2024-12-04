import os
import json
import subprocess
from utils.internet import is_connected
from utils.tasks import execute_task, open_application
from utils.weather import get_weather
from utils.jokes import tell_joke
from utils.gui import run_gui

# Load konfigurasi
CONFIG_FILE = "config.json"

def load_config():
    if not os.path.exists(CONFIG_FILE):
        default_config = {"name": "Arcii", "user": "User"}
        with open(CONFIG_FILE, "w") as f:
            json.dump(default_config, f)
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def main():
    config = load_config()
    arcii_name = config["name"]
    user_name = config["user"]

    print(f"Hello, {user_name}! I am {arcii_name}. How can I assist you today?")
    while True:
        command = input("You: ").lower()

        if "exit" in command:
            print(f"{arcii_name}: Goodbye, {user_name}!")
            break
        elif "joke" in command:
            print(tell_joke())
        elif "weather" in command:
            if is_connected():
                city = input(f"{arcii_name}: Which city? ")
                print(get_weather(city))
            else:
                print(f"{arcii_name}: Sorry, no internet connection.")
        elif "open" in command:
            app = command.replace("open", "").strip()
            open_application(app)
        elif "run gui" in command:
            run_gui()
        else:
            execute_task(command)

if __name__ == "__main__":
    main()

