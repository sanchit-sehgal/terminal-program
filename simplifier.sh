#!/bin/bash

sudo pacman -S git --noconfirm
sudo pacman -S python --noconfirm
sudo pacman -S tk --noconfirm
sudo pacman -S tensorflow --noconfirm
sudo pacman -Syy && sudo pacman -Syu --noconfirm

pip install pyautogui
pip install PyDictionary
pip install pynput

cd main
python runner.py
