#!/bin/bash

read -p "Are you sure you want to delete CAST? (y/N): " answer
answer=${answer:-n}

if [ "$answer" != "y" ] && [ "$answer" != "Y" ]; then
    echo "The removal process has been cancelled"
    exit 0
fi

rm -rf ~/.local/share/cast/
rm -rf ~/.config/cast/
rm -f ~/.local/bin/cast

sed -i '/cast/d' ~/.bashrc 2>/dev/null
sed -i '/cast/d' ~/.zshrc 2>/dev/null

read -p "Press Enter to Continue..."
