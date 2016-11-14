Title: A short guide for new VIM users
Date: 2016-11-29 16:30
Category: vim
Tags: vim
Authors: Rok Povšič

VIM is a text editor that makes writing code MUCH more enjoyable. Once you learn it you can't believe how people can code without it. It's like driving a new BMW opposed to an old Peugeot. Everything is just smooth and fast. And unlike BMW, it's free! Watching another programmer write code without using VIM is *almost* like watching your mother type two sentences using two fingers which takes 5 minutes. You just want to say: give me the keyboard, I'll do it for you. The programmer uses UP, DOWN, LEFT and RIGHT keys, reaches for the mouse a lot, repeats certain actions a lot and might even know how to cleverly use HOME, END, PGUP and PGDOWN keys. But compared to VIM it's just too slow and awkward.

The best thing about VIM is that you don't even need to use the original program! You just install a VIM plugin for your favorite editor (such plugin exists for all major editors, including Visual Studio, all JetBrains editors, Atom, Sublime, ...) and you get all the functionality of the original VIM editor.

## Modes
When writing code (or some other text) in a regular editor the key you press will appear on screen right away. Using VIM this will happen only if you are in so called *insert* mode. When in this mode, VIM behaves as any other editor. When starting VIM, it is in *normal* mode. To enter *insert* mode, simply press **i**. Now you can type anything you want. To exit *insert* mode and go back to *normal* mode, press **ESC**.

## Moving around
So why would is this *normal* mode even needed if we use keyboard to type characters on the screen and the only way we can do that is by being in the *insert* mode. Well, VIM makes the keyboard much more versatile tool. For example, when in *normal* mode, you can use keys **H**, **J**, **K** and **L** in order to move LEFT, DOWN, UP and RIGHT, respectively. That's very useful since it removes the need to always move your hand to the arrow keys. It takes some time to get used to but once you know it, it's hard to go back. When the hands are in the typing position (left index finger on **F** and right index finger on **J**) it's much more convenient to simply press **ESC** (which I even virtually switched with **CAPS LOCK** to have it closer to the standard position) and use **H**, **J**, **K** and **L**.

Moving to the start of the next word is done by pressing **W** and moving to the start of previous word by pressing **B**. It's similar to pressing **CTRL + LEFT/RIGHT** when using regular editor, without the need to move right hand away from natural position and pressing two keys at the same time.

Another thing I use a lot is pressing **{** and **}** which will jump the cursor to previous and to next paragraph (in **normal** mode of course) and pressing **0** and **$$** which move the cursor to the beginning or end of the line you are currently on.

I think that this alone is worth using VIM when writing code or anything else.

## Copying, deleting and pasting lines
When writing code it's common to copy a line and paste it somewhere else. Copying a line is done by pressing **YY** (i.e. pressing **Y** twice). After that you can move anywhere else and with pressing **P** the line will be pasted under the line your cursor is on.

Deleting a line is done by pressing **DD**. We can imagine it's similar to cutting a line as you can still paste it using **P**.

## Undo / Redo
Undoing the last command (i.e. inserting, deleting, pasting, etc.) is done by pressing **U**. The redo command is **CTRL + R**.

## Selecting lines
Another very useful command is **SHIFT + V** which starts to select lines. After moving up or down (preferably with **K** or **J**) you press **Y** to copy them. Now you can move to some other place and press **P** to paste copied lines (use **D** instead of **Y** to delete them).

## Saving positions and jumping
Wherever your cursor is located you can press **M** followed by any character an the position will be saved. After that you can press **'** followed by the character you used previously and your cursor will jump to saved position. Very useful!

## Searching
Searching is done by simply pressing **/**, typing the word to search for and pressing **ENTER**. The cursor is moved to the first found word. After that, pressing **N** will jump to the next found word (and **SHIFT + N** will jump to the previous found word).

## Replacing

## Repeating commands

## Other small things

## How to learn all this?
There's no need to learn everything to start using vim. I think VIM has major advantages even when you use only a small subset of it. Simply start by installing a VIM plugin for your code editor and using mostly *insert* mode and maybe **H**, **J**, **K** and **L** (the keys to move in different directions, remember?) in the *normal* mode here and there
