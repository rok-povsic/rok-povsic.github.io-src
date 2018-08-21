Title: A short guide for new VIM users
Date: 2016-12-10 8:30
Category: vim
Tags: vim
Authors: Rok Povšič

VIM is a text editor that makes writing code MUCH more enjoyable. After using it for a long time it's almost hard to believe how people can write code without it. It's like driving a new BMW opposed to an old Peugeot. Everything is just smooth and fast. And unlike BMW, it's free! Watching another programmer write code without using VIM is *almost* like watching someone type using two fingers (one with each hand). You just want to say: give me the keyboard, I'll do it for you. The programmer uses UP, DOWN, LEFT and RIGHT keys, reaches for the mouse a lot, repeats certain actions a lot and is most likely very efficient and clever with the use of HOME, END, PGUP and PGDOWN keys. But compared to VIM it's all slow and awkward.

The best thing about VIM is that you don't even need to use the original program! You just install a VIM plugin for your favorite editor (such plugin exists for all major editors, including Visual Studio, all JetBrains editors, Atom, Sublime, ...) and you get all the functionality of the original VIM editor. What's great here is that using VIM gives you a consistency across all the editors. You don't need to remember as much specific stuff for each editor (i.e. what's the shortcut for Redo in this IDE, again?) - VIM is the same in all of them.

<!-- PELICAN_END_SUMMARY -->

## Modes
When writing code (or some other text) in a regular editor the key, the keys you press appear on the screen right away. Using VIM this will happen only if you are in so called *insert* mode. When in this mode, VIM behaves as any other editor. After VIM has just started, it is in *normal* mode. If you simply want to write some text, press **i** to enter *insert* mode. Now you can type anything you want. To exit *insert* mode and go back to *normal* mode, press **ESC**.

![]({filename}/images/vim_short/modes.gif)

## Moving around
So why would is this *normal* mode even needed if we use keyboard to type characters on the screen and the only way we can do that is by being in the *insert* mode. Well, VIM makes the keyboard much more versatile tool. For example, when in *normal* mode, you can use keys **H**, **J**, **K** and **L** in order to move LEFT, DOWN, UP and RIGHT, respectively. That's very useful since it removes the need to always move your hand to the arrow keys. It takes some time to get used to but once you know it, it's hard to go back. When the hands are in the typing position (left index finger on **F** and right index finger on **J**) it's much more convenient to simply press **ESC** (which I even virtually switched with **CAPS LOCK** to have it closer to the standard position) and use **H**, **J**, **K** and **L**.

Moving to the start of the next word is done by pressing **W** and moving to the start of previous word by pressing **B**. It's similar to pressing **CTRL + LEFT/RIGHT** when using regular editor, without the need to move right hand away from natural position and pressing two keys at the same time.

Another thing I use a lot is pressing **{** and **}** which will jump the cursor to previous and to next paragraph (in **normal** mode of course) and pressing **0** and **$$** which move the cursor to the beginning or end of the line you are currently on.

I think that this alone is worth using VIM when writing code or anything else.

![]({filename}/images/vim_short/hjkl.gif)

## Copying, deleting and pasting lines
When writing code it's common to copy a line and paste it somewhere else. Copying a line is done by pressing **YY** (i.e. pressing **Y** twice). After that you can move anywhere else and with pressing **P** the line will be pasted under the line your cursor is on.

Deleting a line is done by pressing **DD**. We can imagine it's similar to cutting a line as you can still paste it using **P**.

![]({filename}/images/vim_short/copy_paste.gif)

## Undo / Redo
Undoing the last command (i.e. inserting, deleting, pasting, etc.) is done by pressing **U**. The redo command is **CTRL + R**.

![]({filename}/images/vim_short/undo.gif)

## Selecting lines
Another very useful command is **SHIFT + V** which starts to select lines. After moving up or down (preferably with **K** or **J**) you press **Y** to copy them. Now you can move to some other place and press **P** to paste copied lines (use **D** instead of **Y** to delete them).

![]({filename}/images/vim_short/selecting.gif)

## Saving positions and jumping
Wherever your cursor is located you can press **M** followed by any character an the position will be saved. After that you can press **'** followed by the character you used previously and your cursor will jump to saved position. Very useful!

![]({filename}/images/vim_short/save.gif)

## Searching
Searching is done by simply pressing **/**, typing the word to search for and pressing **ENTER**. The cursor is moved to the first found word. After that, pressing **N** will move the cursor to the next found word (and **SHIFT + N** will move it to the previous found word).

![]({filename}/images/vim_short/searching.gif)

## Replacing
Often you need to replace all words with some other words in a given text. First, you select the text (by using **SHIFT + V**, remember?) and then typing this (without the < and >): **:s/&lt;text to search>/&lt;text to replace it with>/g**. It might sound complex but once you get used to it it's so much faster and easier than using the default Find & Replace functionality of whatever IDE you are using at this moment.

![]({filename}/images/vim_short/replacing.gif)

## Other small things
Pressing **SHIFT + I** will open *insert* mode in the beginning of the row and **SHIFT + A** will open *insert* mode at the end of the row.

![]({filename}/images/vim_short/other.gif)

## Repeating commands machine
Repeating commands is where VIM really shows its power. Whatever command you've seen so far, you can save its execution sequence and repeat it. This is huge! First you record a command or a sequence of commands by first pressing **Q&lt;some key, say A>**, executing the commands, and then pressing **Q** to end the execution and save it. Then you can replay it by pressing **&lt;number of times to repeat>@a**.

Let's look at an example. Say I have these lines in my editor and I want to add parenthesis around them, with a comma on the right and a tab on the left.

Marlon Brando
Al Pacino
James Caan
Richard S. Castellano
Robert Duvall
Sterling Hayden

I could do it by hand or I could utilize the great power of VIM and do it singlehandedly, wizard-style. I'll do it by first moving to the first line and pressing **QA** - that will start recording my commands under the key A. Then I do **SHIFT + I** to move to the beginning of the line and open *normal* mode, followed by pressing TAB and ". Then I press **ESC** to exit *insert* mode and return to *normal* mode and do **SHIFT + A** to open *insert* mode at the end of the line. Next, I press " and ,. I exit *insert* mode again and press **J** to move one line down. My execution sequence is finished so I complete it by pressing **Q**.

Now VIM has remember the whole execution and will execute it any number of times. I simply do **5@A** and the execution will be repeated 5 times, fixing all my lines.

![]({filename}/images/vim_short/repeating.gif)

## How to learn all this?
There's no need to learn everything to start using VIM. I think that VIM has major advantages even when you use only a small subset of the provided functionality. Simply start using it by installing a VIM plugin for your code editor and using mostly *insert* mode and maybe **H**, **J**, **K** and **L** (the keys to move in different directions, remember?) in the *normal* mode instead of the arrow keys. After you get a grasp of that, add some other thing that sounds interesting. It's like driving a car - at first it's hard and complex, after a few months it's completely automatic and you don't even think about it.
