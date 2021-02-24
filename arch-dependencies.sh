#!/bin/bash

echo "Installing Dependencies... "
echo ""

sudo pacman -S python --noconfirm
sudo pacman -S tk --noconfirm
sudo pacman -S tensorflow --noconfirm
sudo pacman -S w3m --noconfirm
sudo pacman -S curl --noconfirm
sudo pacman -S nnn --noconfirm
sudo pacman -S sl --noconfirm
git clone https://aur.archlinux.org/nudoku-git.git
cd nudoku-git
makepkg -si --noconfirm
cd -
git clone https://aur.archlinux.org/bastet.git
cd bastet
makepkg -si --noconfirm
cd -
sudo pacman -S pydf --noconfirm
sudo pacman -S hwinfo --noconfirm
pip install pyautogui
pip install PyDictionary
pip install pynput
pip install pygame

echo ""
echo "All dependencies installed."
