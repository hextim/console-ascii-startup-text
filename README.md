<div align="center">

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![gnu](https://img.shields.io/badge/gnu-%23A42E2B.svg?style=for-the-badge&logo=gnu&logoColor=white)](https://www.gnu.org/licenses/gpl-3.0.html)
[![Linux](https://img.shields.io/badge/Linux_Utility-FCC624?style=for-the-badge&logo=linux&logoColor=black)](https://kernel.org/)
![Version](https://img.shields.io/badge/ver._0.0.0-4A4E51?style=for-the-badge&logoColor=white)

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

## Manual start

To launch the utility, you need to navigate to the src/ directory and enter the following command:

```bash
python3 main.py
```

## Manual installation

If you want to set up a program to launch automatically, you simply need to add a single line to the .bashrc or .zshrc file located in the user's home directory:

``` bash
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

## Automatic installation using a script

In the making
