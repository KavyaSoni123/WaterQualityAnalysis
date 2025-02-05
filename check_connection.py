import ee
from config import PROJECT_ID
from colorama import Fore, Style, init
import time

init(autoreset=True)


def cool_loading_animation():
    message = "Trying to connect 🥵🥵🥵..."
    for i in range(4):  # Loop for creating animation
        print(
            Fore.YELLOW + f"{message} {'🍆🍑' * i}", end="\r"
        )  # Overwrites the line each time
        time.sleep(0.5)  # Pause for a bit to create the animation effect

    print(Fore.GREEN + "✅ Connection Success! ✅")  # Final message after animation


try:
    ee.Initialize(project=PROJECT_ID)
    print(Fore.BLUE + "🌍 Earth Engine initialized successfully! 🌍" + Style.RESET_ALL)
    cool_loading_animation()
except Exception as e:
    print("Error initializing Earth Engine:", e)
