Title: Using PyCharm without a mouse
Date: 2016-10-29 16:30
Category: pycharm
Tags: pycharm, shortcuts
Authors: Rok Povšič

I've been always fan of minimizing mouse/touchpad usage when programming. There is a certain kind of satisfaction when you are able to do everything with the keyboard. You get the feeling of being agile, swift. It's a sign of mastery. There's no unnecessary movement and unnecessary time and muscle power spent. Watching another programmer use their keyboard solely and be fast doing it makes you respect them more. Watching them grab the mouse a lot and wait for them to find the mouse cursor is sometimes even a little painful.

## Run the program
So how do you go about using keyboard more and using mouse less? Well, start off by learning how to run your program with only the keyboard.

How to do that? To run currently open file press **CTRL + SHIFT + F10**. To run lastly open file, even if you are currently in another file, press **SHIFT + F10**. To run an arbitrarily chosen file press **SHIFT + ALT + F10** to open a dialog box where you select which file to run.

#### Hide output window
After you run the program output window will appear if it wasn't shown before. Unlike in Visual Studio, this output window will not hide automatically. This can be annoying if you want a large screen space for code. Well, there's a simple shortcut for hiding a window you are in (besides grabbing the mouse and clicking hide window button on top right) and it's **SHIFT + ESC**. Press that after running the program and output window will close leaving your focus in the code and you can start typing again.

## Go to a file
Press **CTRL + SHIFT + N** and start writing name of a file to jump to it. I've remapped the shortcut to  **CTRL + T** to be equal to the same shortcut in ReSharper (Visual Studio).

## Refactoring
The best advantage of PyCharm is its refactoring capability. Being positioned on a variable/function/class and doing **CTRL + SHIFT + ALT + T**. It gives you lots of refactoring options such as:

- rename,
- inline,
- extract variable, method,
- change method signature.

These PyCharm refactoring functionalities are not only huge time savers but also, unlike we humans, they don't make mistakes.

Since this shortcut involves four keys, I've remapped it to **CTRL + SHIFT + R** (same as refactoring using ReSharper in Visual Studio).

#### Confirm refactoring
When refactoring, PyCharm sometimes requires a confirmation of the refactoring (e.g. after renaming a function). The button you have to click says "Do Refactor" and it's located in another window. This used to annoy me a lot since I didn't know how to press this button via keyboard. But I found the solution. After doing the renaming, simply press **ALT + D** and the "Do Refactor" button will be clicked. After that press **SHIFT + ESC** to close the refactoring window.

## Toggle full screen
You can add your own shortcut to toggle full screen if you go to Settings -> Keymap (shorcut to doing that is pressing **CTRL + ALT + S** and typing **Keymap**) since there is no default shortcut.

But you can still do it with your keyboard pretty fast by pressing **ALT + V** to open the View menu and pressing **down arrow** and **Enter**.

I got used to that even though it's not the completely fastest way although it's pretty fast.

## You can't do everything with a keyboard
I don't use solely keyboard for every single thing in PyCharm. I still use the mouse to scroll up and down in the output window. I use the mouse to open a file for which I am not exactly sure what its name is but I know where it's located in the folder hierarchy. My goal is not to never use the mouse but to not use it when there's a fast and comfortable alternative. There is a lot of these kinds of shortcuts and they keep surprising you if you look for them.
