## About Terminal-Simplifier
This program aims to simplify use of the terminal for those with little to no experience using the terminal. In many operating systems, the terminal is always seen as the most "hacky"- several commands can destroy your OS and ruin your computer. In reality, however, the terminal is an extremely simple element in your OS and can greatly increase your productivity if used correctly. In order to use the terminal to its full potential however, you would _usually_ have to learn several commands. By using terminal-simplifier, there's no need to learn the commands- you can let the computer do it all for you. 

Installing this program may seem tricky, but by using the installation guide below, you can have the program up and running in only 10-15 minutes. Once you have it installed, that's it! The terminal is at your command- from productivity commands to playing games, you can do nearly everything with this program. To get started with the installation guide below, open the terminal (**Ctrl+Alt+T** in most cases).

## Installation Guide (Arch-based Distributions)

##### Install Git
Once you have opened your terminal, we need to first install git. In Arch Linux based distributions, git can be installed by typing the following code:
```
sudo pacman -S git --noconfirm
```

Once you have installed git, we need to install Python.
##### Install Python (and Pip)
To install Python (and its package manager- pip), type the following code into your terminal:
```
sudo pacman -S python --noconfirm
```
This will automatically download the latest version of Python onto your system. This is essential to run the program.

##### Install Required Dependencies
To install the dependencies, we first need to clone this repository into our terminal. To do so, press the green code button as seen in the following image:
![alt text](screenshots/codebutton.png)

Make sure you have selected HTTPS as shown below. Then, press the clipboard button to copy the repository link, as seen here:



![alt text](screenshots/clipboardbutton.png)

Once you have copied the link to the repository, we need to head back to the terminal. On a new line, we need to type the following:
```
git clone **link**
```
where link is our copied repository link. We can paste this by pressing **Ctrl+Shift+V**. When you enter this command, you should see something resembling this:

![alt text](screenshots/clonedrepo.png)

Once we have cloned into the repository, type the following command into your terminal:
```
cd terminal-simplifier
```

We are now in terminal-simplifier directory which we have just created. Once we have entered the directory, we need to execute our dependency installer by typing the following commands into our terminal:
```
chmod u+x arch-dependencies.sh
```
```
./arch-dependencies.sh
```
Once this command is finished executing, we have successfully installed Terminal Simplifier!

## Installation Guide (Ubuntu + Debain-based Distributions)

##### Install Git

##### Install Python (and Pip)

##### Install Required Dependencies

## Run Terminal-Simplifier

##### Arch (and Arch-based Distributions)

##### Debian/Ubuntu (and Debian-based Distributions)

## Troubleshooting Guide

## About the Creator

## License
This program and its corresponding code is covered under the MIT License. For more information on the license, [view LICENSE.md here.](https://github.com/sanchit-sehgal/terminal-simplifier/blob/main/LICENSE)

## Wiki
For this repository's wiki, view [this page.](https://github.com/sanchit-sehgal/terminal-simplifier/wiki/Introduction)
