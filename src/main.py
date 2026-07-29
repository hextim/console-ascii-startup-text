import subprocess
import os
import sys
import json

config_dir = os.path.expanduser("~/.config/cast")
install_dir = os.path.expanduser("~/.local/share/cast")
script_dir = os.path.dirname(os.path.abspath(__file__))


if script_dir == install_dir:
    config_path = os.path.join(config_dir, "config.json")
else:
    config_path = os.path.join(script_dir, "config.json")

# checking config
try:
    with open(config_path, "r", encoding="utf-8") as file:
        config_data = json.load(file) # converting the config content into a standard python dictionary
except (FileNotFoundError, json.JSONDecodeError):
    sys.exit("ERROR: failed to open the configuration file")

# transferring data from the config to standard variables for convenience
logo = config_data["logo"]
logo_margin = config_data["logo_margin"]
text_margin = config_data["text_margin"]

# check for the presence of the figlet command
try:
    text = subprocess.check_output(f"figlet -f {config_data["font"]} {config_data["text"]}", shell=True, text=True, stderr=subprocess.STDOUT).splitlines() # ASCII text generation (the figlet utility is available exclusively on Linux distributions)
except subprocess.CalledProcessError:
    sys.exit("ERROR: figlet command not found")

# list cursors
logo_index = 0
text_index = 0

max_logo_width = len(max(logo, key=len)) if logo else 0 # we find the maximum width of the ASCII logo
total_lines = max(len(logo) + logo_margin, len(text) + text_margin) # total number of lines for image display

# image output
print("\n" * config_data["top_margin"])
for i in range(total_lines):

    print(" " * config_data["edge_margin"], end="")
    
    # logo display
    if logo_margin <= i < logo_margin + len(logo):
        print(logo[logo_index] + " " * (max_logo_width - len(logo[logo_index])), end="")
        logo_index += 1
    else:
        print(" " * max_logo_width, end="")

    print(" " * config_data["middle_margin"], end="")
    
    # text display
    if text_margin <= i < text_margin + len(text):
        print(text[text_index])
        text_index += 1
    else:
        print()
print("\n" * config_data["bottom_margin"])
