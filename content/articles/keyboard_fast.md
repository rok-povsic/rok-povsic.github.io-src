Title: Keyboard tricks to write code faster
Date: 2016-10-31 10:44
Category: typing
Tags: typing, fast
Authors: Rok Povšič

## Using English keyboard layout
Using any keyboard layout other than English may be less optimal for programming, at least that was my experience when compared to using Slovenian and German keyboard layouts to write code. Switching to the English layout made a great difference for me. It's simply faster to reach commonly used characters such as []{};:,@""<>= compared some (maybe all) other layouts. I've trained myself to always use English keyboard when programming and when writing in English language in general (such as now).  

<!-- PELICAN_END_SUMMARY -->

When writing in Slovenian language I switch the keyboard layout to Slovenian and continue seamlessly as nothing changed. Then only keys that I sometimes use wrong on Slovenian layout are letters Y and Z which are for some reason switched in Slovenian keyboard layout.

## Try using VIM
The next level mastery is not only to stop reaching for a mouse but also stop reaching for the movement keys (UP, DOWN, LEFT and RIGHT). They are also quite far away from the keys you use to do the actual writing. When programming we use movement keys a lot and minimizing or entirely removing the need to access them saves time and thousands of unnecessary hand movements.

## Switch Caps Lock and Esc keys
Since I press Esc much more than Caps Lock, I switched the two keys (functionally, not physically). I use software called [SharpKeys](https://sharpkeys.codeplex.com/) to do that. It's much more enjoyable to use the keyboard like that.

I also considered switching Backspace with some other key but haven't so far found a good replacement. I thought about Right Shift, which I don't use a lot, but it's not that of a good improvement. 

## Shorter delay when holding a key
When programming you often have to hold down a certain key - one of the arrow keys, backspace, or, if you use VIM, one of the keys h, j, k, l, w, b, etc. I've found out that, for me, the delay between the appearance of the first character and the following is too great. I've reduced the delay to 250ms and typing seems much more responsive and enjoyable. At this speed it's still quite rare for me to produce a duplicated key when I don't intend to do one.

In Linux, the delay is set by adding the following line to `.bashrc`:
```python
xset r rate 250
```
