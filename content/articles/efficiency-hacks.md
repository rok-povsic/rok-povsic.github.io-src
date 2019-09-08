Title: Efficiency hacks for programmers
Date: 2019-09-08 11:04
Category: efficiency
Tags: programming, efficiency, hacks, tips, tricks, linux, gnome, vim, extensions
Authors: Rok Povšič

Over the years, I've found a number of *efficiency hacks* which make using the computer as a software developer much more smooth and elegant. This involves how I use the OS, the IDE, and other tools. I've found it pays to sharpen the saw and make the flow of work as hurdle-free as possible, especially for the tasks that are repeated many times. The cost of setting things up and learning to use any particular hack non-trivial but fixed, and the benefit is ongoing. In this post, I describe the hacks that made the most impact for me.

<!-- PELICAN_END_SUMMARY -->

## Table of Concents

<div>
    <ol>
        <li>
            <a href="#1-vim-everywhere">Vim everywhere</a>
            <ul>
                <li><a href="#programming">Programming</a> </li>
                <li><a href="#browser">Browser</a> </li>
                <li><a href="#terminal">Terminal</a> </li>
            </ul>
        </li>
        <li>
            <a href="#2-terminal-usage">Terminal usage</a>
            <ul>
                <li><a href="#better-command-history-with-ctrlr">Better command history with CTRL+R</a> </li>
                <li><a href="#git-command-line-shortcuts">Git command line shortcuts</a> </li>
            </ul>
        </li>
        <li>
            <a href="#3-gnome-shell">Gnome Shell</a>
            <ul>
                <li><a href="#gtile">Gtile</a> </li>
                <li><a href="#impatience">Impatience</a> </li>
                <li><a href="#drop-down-terminal">Drop down terminal</a> </li>
                <li><a href="#hide-top-bar-no-title-bar">Hide top bar / No title bar</a> </li>
                <li><a href="#gnome-shell-workspaces">Gnome Shell workspaces</a> </li>
            </ul>
        </li>
        <li><a href="#4-conclusion">Summary</a></li>
    </ul>
</div>


My observation is that efficiency of using a computer *is* important when it comes to software development. Even if the process of programming involves a lot (or even the majority) of thinking instead of typing, the ability to move these thoughts into computer as quickly as possible is of great benefit. How quickly would we build software if we could make the code appear, move around, refactor, delete instantly, all with the power of our thoughts? We cannot do that (at least not in in 2019), but we can definitely make improvements in how we use the currently available interface - the keyboard.

> Warning: Certain tips only apply to *nix system, and some only to the Gnome window manager.

---------------

## 1. Vim everywhere

### Programming

I use Vim-mode everywhere I need to type text. This includes programming, of course, but other interfaces as well. Most modern IDEs have some variant of a "Vim mode" or a "Vim plugin" (at least do the JetBrains IDEs, Visual Studio, Eclipse, VS Code, Sublime, Atom). While these are only simulations of the original Vim and do not behave *exactly* the same in all cases, the commands that I actually use are available and mostly identical. Some tinkering is required to resolve any keyboard shortcuts conflicts between the IDE and Vim. But once this is done, programming is faster, and in my experience, more enjoyable.

<video width="600" src="videos/efficiency-hacks/vim.webm" controls preload="metadata"></video>

### Browser

I also use a Vim extension in the browsers I use, both in [Firefox](https://addons.mozilla.org/en-US/firefox/addon/vimium-ff/) and [Chrome](https://chrome.google.com/webstore/detail/vimium/dbepggeogbaibhgnhhndojpepiihcmeb). It makes it possible to browse without leaving the home row position, using K/J to move up/down (I use U/D do move up/down with greater speed), and using F + some-key-combination to visit links. I've also added shortcuts ALT+H and ALT+L to move to back/forward, as I have the same shortcuts for Back and Forward in my IDEs as well.

<video width="600" src="videos/efficiency-hacks/browser.webm" controls preload="metadata"></video>

### Terminal

I've also have enabled [vi-mode](http://vim.wikia.com/wiki/Use_vi_shortcuts_in_terminal) in my Bash terminal. By default, you're in the insert mode, so the command line behaves as it would on some other machine. But you can, of course, switch to the command mode pressing ESC. This comes in handy when there's a long command I'm working on, and can quickly move between the words (with W and B), delete words (DW etc.), insert and beginning/end of the line with I and A, etc.

<video width="600" src="videos/efficiency-hacks/terminal.webm" controls preload="metadata"></video>

---------------

## 2. Terminal usage

### Better command history with CTRL+R

[fzf](https://github.com/junegunn/fzf) is an excellent tool providing fuzzy (i.e. non-exact) search. This comes in handy when searching for a command which has been executed in the past. The default CTRL+R shell already gives the functionality to scroll through the last commands, and fzf is an improved replacement of that, providing fuzzy search of past commands, and giving a better overview of the history last few commands.

<video width="600" src="videos/efficiency-hacks/fzf.webm" controls preload="metadata"></video>

### Git command line shortcuts

One of the terminal commands I use the most is `git`. But typing out the `git <something>` commands many times each day became repetitive, so I've set up a number of Git aliases (I got the idea from [this blog post](https://jonsuh.com/blog/git-command-line-shortcuts/)).

The shortcuts I mostly use are:

- `gaa` (`git add .`), 
- `gcm` (`git commit --message`), 
- `gco` (`git checkout`),
- `gcob` (`git checkout --branch`),
- `gd` (`git diff`), 
- `gds` (`git diff --staged`), 
- `gld` (`git log --pretty=format:"%h %ad %s" --date=short --all`),
- `gpoh` (`git push origin HEAD`), 
- `grb` (`git rebase`), 
- `grba` (`git rebase --abort`), 
- `grbc` (`git rebase --continue`),
- `gs` (`git status`).

I've also set up auto-completion, so when typing `gco mas<TAB>`, `master` auto-completes. Here's what to put to `~/.bash_aliases` (or some other place from where your terminal loads custom code from) to set all this up: [Git Aliases]({filename}/pages/git-aliases.md)

<video width="600" src="videos/efficiency-hacks/git-aliases.webm" controls preload="metadata"></video>

---------------

## 3. Gnome Shell

Gnome Shell has an excellent [extension system](https://extensions.gnome.org/) which provides some truly great extensions. Here's a couple I use.


### Gtile

[Gtile](https://extensions.gnome.org/extension/28/gtile/) provides the functionality of re-positioning of windows within a workspace, similar to what is done when using a tiled window manager. Instead of grabbing a mouse and dragging/resizing a window, use one of the numerous Gtile shortcuts I've set up that position my windows to the places I most often want them to be. For example, I've set up the shortcuts `CTRL+WIN+U/I/N/M` to move the currently focused window to top-left/top-right/bottom-left/bottom-right quarter of the screen, respectively.

<video width="600" src="videos/efficiency-hacks/gtile.webm" controls preload="metadata"></video>

### Impatience

To speed up animations that take place when switching between workspaces (see below), I use the extension called [Impatiance](https://extensions.gnome.org/extension/277/impatience/) which makes animations go faster.

### Drop down terminal

The [Drop down terminal](https://extensions.gnome.org/extension/442/drop-down-terminal/) extension displays a quick terminal window on the top of the screen, after pressing `CTRL+ALT+F11`.

<video width="600" src="videos/efficiency-hacks/top-terminal.webm" controls preload="metadata"></video>

### Hide top bar / No title bar

The [Hide top bar](https://extensions.gnome.org/extension/545/hide-top-bar/) and [No title bar](https://extensions.gnome.org/extension/1267/no-title-bar/) extensions make every program, when on full-screen, use all the available screen real-estate. To me, immersion is increased when the display is showing strictly what's necessary for work to get done.

### Gnome Shell workspaces

This is actually not an extension but a part of the base Gnome system. It allows you to have windows in multiple workspaces, between which you can move using a keyboard or a mouse. I use 4 workspaces in one row and move between them using shortcuts `CTRL+ALT+H`/`CTRL+ALT+L` to switch to a workspace on the left/right, and `CTRL+SHIFT+ALT+H/L` to move a window to a workspace on the left/right. I usually use the first workspace to host IDEs and terminals, the second to host Firefox and Slack, and the other two for various less-accessed programs such as KeePass. Using workspaces means in such a way means better organization and fewer pressings of `ALT+TAB`.

---------------

## 4. Conclusion

These efficiency hacks did make my computer usage flow smoother and more enjoyable. It takes time to set everything up, but what I've described here is more or less a fixed cost. One could spend _too much_ time if tinkering with it all the time, but from my experience once I add a tool and get used to it, the fixed setup costs are soon reimbursed by increased speed and enjoyment. I highly recommend you give some of these a try.
