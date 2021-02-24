#!/bin/bash

echo "Installing Dependencies... "
sudo su
sudo pacman -S python --noconfirm
sudo pacman -S tk --noconfirm
sudo pacman -S tensorflow --noconfirm
sudo pacman -S w3m
sudo pacman -S curl
sudo pacman -S nnn
sudo pacman -S sl
git clone https://aur.archlinux.org/nudoku-git.git
cd nudoku-git
makepkg -si --noconfirm
cd -
git clone https://aur.archlinux.org/bastet.git
cd bastet
makepkg -si --noconfirm
cd -
sudo pacman -S pydf
sudo pacman -S 
pip install pyautogui
pip install PyDictionary
pip install pynput
pip install pygame
exit
