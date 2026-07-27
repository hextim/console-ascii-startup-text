#!/bin/bash

repository="https://raw.githubusercontent.com/hextim/console-ascii-startup-text/main/"

mkdir -p ~/.local/share/cast/ ~/.config/cast/ ~/.local/bin/

curl -sSL "$repository/main.py" -o ~/.local/share/cast/main.py
curl -sSL "$repository/config.json" -o ~/.config/cast/config.json

echo "python3 ~/.local/share/cast/main.py" > ~/.local/bin/cast
chmod +x ~/.local/bin/cast

if ! grep -q "cast" "$HOME/.bashrc" 2>/dev/null; then
  echo 'cast' >> "$HOME/.bashrc"
fi

if ! grep -q "cast" "$HOME/.zshrc" 2>/dev/null; then
  echo 'cast' >> "$HOME/.zshrc"
fi

echo "The installation was successful!"
