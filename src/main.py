# the code is not functional yet

import subprocess
import json

# example logo
# thanks to Joan G. Stark (Spunk) for the logo
ascii_logo = [
    "    .---.",
    "   /     \\",
    "   \\.@-@./",
    "   /`\\_/`\\",
    "  //  _  \\\\",
    " | \\     )|_",
    "/`\\_`>  <_/ \\",
    "\\__/'---'\\__/"
]

# ASCII text generation (the figlet utility is available exclusively on Linux distributions)
ascii_text = subprocess.check_output("figlet linux", shell=True, text=True).splitlines()

# checking config
with open("config.json", "r", encoding="utf-8") as file:
    config_data = json.load(file) # converting the config content into a standard python dictionary

# list cursors
logo_index = 0
text_index = 0

# comparison of object sizes
for i in range(max(len(ascii_logo) + config_data["delay_logo"], len(ascii_text) + config_data["delay_text"]))

    # image output
    (print(ascii_logo[logo_index], end=""), logo_index := logo_index + 1) if config_data["delay_logo"] >= i else " " * len(max(ascii_logo, key=len)), end="")
    print(ascii_text[i] )
