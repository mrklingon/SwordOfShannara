# SwordOfShannara
Microbit programs for a simple "Sword of Shannara" game in python and Makecode.

This is a vastly simplified version of the classic fantasy "The Sword of Shannara." 

* A - move left
* B - move right
* A+B - unleash the Elfstones to destroy a Skull Bearer if one is overhead


 ![sword1](https://github.com/user-attachments/assets/ccaa3176-3253-4b5e-af92-b083bb100574)
Screen above shows "you," representing the hero, Shea Ohmsford who is searching for the Sword of Shannara.
You move left/right through a scrolling landscape (100 cells wide) displayed on the 5x5 LED micro:bit screen.

Overhead are dots that represent the "Skull Bearers" (think Tolkein's Nazgul). If you delay when one is overhead, it will attack and you can lose one of your five lives. So either move past quickly, or hit A+B to unleash the Elfstones to eliminate the Skull Bearer. Faint dots along the bottom of the "screen" represent landscape and serve to show your movement left/right.

Somewhere in the middle of the 100-element landscape is the "Sword" represented by three  lit pixels. 
![sword2](https://github.com/user-attachments/assets/12b6fe3c-66bb-402e-85aa-2b811cba1c85)

Game ends when you either lose all 5 lives, or get to the Sword.

Writing this game in MakeCode served as a preliminary "design," which I sketched out AFTER mostly coding the game:

![image](https://github.com/user-attachments/assets/4afd09ec-2110-4e7a-a1ba-80912922792e)

This lead to rewriting the game in Python, using the excellent Micro:Bit IDE - https://python.microbit.org/v/3
![swordgame](https://github.com/user-attachments/assets/bdbd2d70-2d7d-4520-be40-a45203583b3d)

**Files**

* SwordOfShannara.js - MakeCode Version. Paste  into Makecode editor as Javascript, or go to https://makecode.microbit.org/_LHjHeCiaMavM
* SwordOfShannara.py - Python version to enter into https://python.microbit.org/v/3
* SwordOfShannara.hex - can be loaded directly to Micro:Bit *or* opened in https://python.microbit.org/v/3 
