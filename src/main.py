import subprocess
import json

# checking config
with open("config.json", "r", encoding="utf-8") as file:
    config_data = json.load(file) # converting the config content into a standard python dictionary

logo = config_data["logo"]

# ASCII text generation (the figlet utility is available exclusively on Linux distributions)
text = subprocess.check_output("figlet linux", shell=True, text=True).splitlines()

# list cursors
logo_index = 0
text_index = 0

# comparison of object sizes
for i in range(max(len(logo) + config_data["delay_logo"], len(text) + config_data["delay_text"])):

    # image output
    if (len(logo)+config_data["delay_logo"]-2) <= i >= config_data["delay_logo"]:
        print(logo[logo_index] + (" " * len(max(logo, key=len))), end=""); logo_index += 1
    else:
        print(" " * len(max(logo, key=len)), end="")
    if (len(text)+config_data["delay_text"]-2) <= i >= config_data["delay_logo"]:
        print(text[text_index]); text_index += 1
    print(i)
