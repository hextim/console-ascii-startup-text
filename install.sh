#!/bin/bash

repository="https://raw.githubusercontent.com/hextim/console-ascii-startup-text/main/"

echo "Directory creation..."
mkdir -p ~/.local/share/cast/ ~/.config/cast/ ~/.local/bin/

echo "Installing the source code..."
curl -sSL "$repository/src/main.py" -o ~/.local/share/cast/main.py
curl -sSL "$repository/src/config.json" -o ~/.config/cast/config.json

echo "Installing the utility on the system..."
echo "python3 ~/.local/share/cast/main.py" > ~/.local/bin/cast
chmod +x ~/.local/bin/cast

echo "Adding the program to startup..."
if ! grep -q "cast" "$HOME/.bashrc" 2>/dev/null; then
  echo 'cast' >> "$HOME/.bashrc"
fi

if ! grep -q "cast" "$HOME/.zshrc" 2>/dev/null; then
  echo 'cast' >> "$HOME/.zshrc"
fi

echo "The installation was successful!"
