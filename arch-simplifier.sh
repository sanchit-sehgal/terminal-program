#!/bin/bash

sudo pacman -S python --noconfirm
sudo pacman -S tk --noconfirm
sudo pacman -S tensorflow --noconfirm
sudo pacman -S w3m
sudo pacman -S curl
sudo pacman -Syy && sudo pacman -Syu --noconfirm

pip install pyautogui
pip install PyDictionary
pip install pynput
