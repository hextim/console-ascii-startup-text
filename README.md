<div align="center">

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![gnu](https://img.shields.io/badge/gnu-%23A42E2B.svg?style=for-the-badge&logo=gnu&logoColor=white)](https://www.gnu.org/licenses/gpl-3.0.html)
[![Linux](https://img.shields.io/badge/Linux_Utility-FCC624?style=for-the-badge&logo=linux&logoColor=black)](https://kernel.org/)
[![Version](https://img.shields.io/badge/ver._1.0.0-4A4E51?style=for-the-badge&logoColor=white)](https://github.com/hextim/console-ascii-startup-text/releases)

# CAST (Console ASCII Startup Text)

</div>

CAST is a decorative utility that displays an attractive ASCII image in the console upon startup. The program uses a JSON configuration file, making it easy to customize the appearance of the displayed image.

## Dependencies

To run the program, you need to install Figlet and Python 3. Examples of installation on specific distributions:

```bash
# Fedora
dnf install figlet python3

# Ubuntu/Debian
apt install figlet python3

# Arch
pacman -S figlet python
```

It is recommended to update the databases before installation.

## Automatic installation

For automatic installation, the easiest method is to use `curl`:

```bash
curl -sSL https://raw.githubusercontent.com/hextim/console-ascii-startup-text/main/install.sh | bash
```

## Automatic deletion

Before deletion, it is recommended to navigate to a directory such as `Downloads/` for safety. To install and run the uninstallation script, you need to enter the following commands:

```bash
# Installing the script
curl -sSL https://raw.githubusercontent.com/hextim/console-ascii-startup-text/main/uninstall.sh -o uninstall.sh

# Running it
bash uninstall.sh
```

## Manual start

To launch the utility, you need to navigate to the `src/` directory and enter the following command:

```bash
python3 main.py
```

## Manual installation

Before manual installation, you must move the configuration file to the directory containing `main.py` or to the `~/.config/cast` folder. If you want to set up a program to launch automatically, you simply need to add a single line to the .bashrc or .zshrc file located in the user's home directory:

```bash
# ... (existing content of your .bashrc)

# User specific aliases and functions
if [ -d ~/.bashrc.d ]; then
    for rc in ~/.bashrc.d/*; do
        if [ -f "\$rc" ]; then
            . "\$rc"
        fi
    done
fi
unset rc

# auto-start CAST
python3 /file/path/main.py
```

## Manual removal

For manual removal, you will need to enter a few commands:

```bash
# Deleting directories containing files required for CAST
rm -rf ~/.local/share/cast/
rm -rf ~/.config/cast/
rm -f ~/.local/bin/cast

# Removing CAST from startup
sed -i '/cast/d' ~/.bashrc 2>/dev/null

# If you are using zsh, you will need to add this command as well.
sed -i '/cast/d' ~/.zshrc 2>/dev/null
```
