# About This Program

This program aims to increase the use and productivity of the terminal for those who are uncomfortable or unfamiliar with using the terminal. By running this program, a user (who may be uncomfortable using a terminal) has easier access to automated processes without typing any commands themselves. 

# Installation Purposes (MUST READ)
This program can be installed on all major operating systems including Windows, macOS, and most major Linux distributions (Debian and Arch-based distros, as well as Fedora, centOS, and other SUSE-based distros). The flexibility of this project allows for nearly everyone to become more familiar with processes in their terminal, one of the most powerful tools on a PC. This program is also extremely well-optimized and doesn't use many resources, meaning it can run on older and slower machines. 

For many, the terminal can seem "hacky" and can mess up processes in your PC. This project aims to mitigate that fear and allow users to become more familiar with their terminals, as well as allow ease-of-access for nearly anyone who needs to use their terminal. Using automated processes in Python, this program can do nearly anything on the terminal with minimal input from the user. Furthermore, with new features being added rapidly, the capabilities of this program are expanding and being updated to work with the newest versions of supported operating systems. 

Because this project is contained on GitHub, many users may be uncomfortable downloading the files onto their computer. However, if you follow the concise and helpful installation guides below, you can have the terminal-simplifier program installed and ready to go in only 10-15 minutes, depending on your experience level. 

This program was initially designed for Arch Linux users only- however, I have since created modifications for all other types of Linux distributions and even macOS and Windows. Because this was intended to only work on Arch Linux distributions, however, there may be _some_ bugs. In case of any bugs/glitches that alter the program, please create a pull request on this distribution so I can attend to these bugs.

# Installation Guide (for Linux)

**Step 1: Install Git (for all distros)**

Copy (Ctrl+C) and paste (Ctrl+Shift+V) into your opened terminal. 

- Debain-based Distros: ```sudo apt-get install git```

- Arch-based Distros: ```sudo pacman -S git --noconfirm```

- Fedora-based Distros: ```sudo dnf install git-all```

**Step 2: Install Python (for all distros)**

- Debain-based Distros: 
```
sudo apt update
```
```
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev curl libbz2-dev
```
```
wget https://www.python.org/ftp/python/3.9.1/Python-3.9.1.tgz
```
```
tar -xf Python-3.9.1.tgz
```
```
cd Python-3.9.1
```
```
./configure --enable-optimizations
```
```
make -j 2
```
```
sudo make altinstall
```
- Arch-based Distros:

```
sudo pacman -S python
```
```
sudo pacman -Syy && sudo pacman -Syu --noconfirm
```
- Fedora-based Distros:
```
yum update -y
```
```
yum intsall -y python2
```
_You have now installed Python!_

# Installation Guide (for Windows)

# Installation Guide (for macOS)

# Understanding the Program



# About the Creator
