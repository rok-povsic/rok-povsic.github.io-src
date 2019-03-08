
Title: Linux efficiency hacks for programmers
Date: 2018-12-15 19:08
Category: efficiency
Tags: programming, efficiency
Authors: Rok Povšič

Over the years, I've come up with a number of "efficiency hacks" that make using the computer as a software developer much more efficient and smooth. This involves how I use the OS, the IDE, and other tools.
It pays to "sharpen the saw", i.e. make the flow of work as efficient as possible, especially for the tasks that are done a lot.

<!-- PELICAN_END_SUMMARY -->

My observation is that efficiency of using a computer *is* important when it comes to software development. Even if the process of programming involves a lot (or even the majority) of thinking instead of typing, the ability to move these thoughts into computer as quickly as possible is of great benefit. How quickly would we build software if we could instantly make code appear, move it around, refactor it, delete it, with our thoughts? We can't do that in 2019, but we can definitely make improvements in how we use the currently available interface - the keyboard.

Some of the tips here can only be applied in the Gnome environment, and some, more generally, only on Linux, but if you're using some other environment you may get something out of this as well.

## Vim everywhere

I use Vim-mode everywhere I need to type text, especially when programming. Most of the modern IDEs have some variant of a "Vim mode" or a "Vim plugin" (the JetBrains IDEs, Visual Studio, Eclipse, VS Code, Sublime, Atom). I found out they do not always behave *exactly* the same as the original Vim, but in the majority of cases they do. Since usually some keyboard shortcuts conflicts occur between the IDE and Vim, you have to take some time to set them up. But once this is done, programming is much more enjoyable.

I also use a Vim extension in the browsers I use, both in [Firefox](https://addons.mozilla.org/en-US/firefox/addon/vimium-ff/) and [Chrome](https://chrome.google.com/webstore/detail/vimium/dbepggeogbaibhgnhhndojpepiihcmeb). It makes it possible to browse without leaving the home row position, using K/J to move up/down, and using F (+ some key combination) to visit links. I've also added shortcuts ALT+H and ALT+L to move to previous/next page.

I've also have enabled [vi-mode](http://vim.wikia.com/wiki/Use_vi_shortcuts_in_terminal) in my Bash terminal. By default, you're in the insert mode, so it behaves as you'd expect, but you can go to the command mode pressing ESC. This comes in handy when there's a long command I'm working on.

## Terminal usage

### History with CTRL+R

### Git command line shortcuts

The terminal program I use the most is most likely Git. Typing out the commands became repetitive, so I've set up a number of Git aliases (I got the idea from [this blog post](https://jonsuh.com/blog/git-command-line-shortcuts/)). I've also added auto-completion. Here's what I have in `~/.bash_aliases` to set this up:

```bash
# ----------------------
# Git Aliases
# ----------------------
[ -f /usr/share/bash-completion/completions/git ] && . /usr/share/bash-completion/completions/git
alias ga='git add'
__git_complete ga _git_add
alias gaa='git add .'
__git_complete gaa _git_add
alias gaaa='git add --all'
__git_complete gaaa _git_add
alias gau='git add --update'
__git_complete gau _git_add
alias gb='git branch'
__git_complete gb _git_branch
alias gbd='git branch --delete '
__git_complete gbd _git_branch
alias g="git"
__git_complete g _git
alias gc='git commit'
__git_complete gc _git_commit
alias gca='git commit --amend'
__git_complete gca _git_commit
alias gcm='git commit --message'
__git_complete gca _git_commit
alias gcf='git commit --fixup'
__git_complete gca _git_commit
alias gco='git checkout'
__git_complete gco _git_checkout
alias gcob='git checkout -b'
__git_complete gcob _git_checkout
alias gcom='git checkout master'
__git_complete gcom _git_checkout
alias gcos='git checkout staging'
__git_complete gcos _git_checkout
alias gcod='git checkout develop'
__git_complete gcod _git_checkout
alias gd='git diff'
__git_complete gd _git_diff
alias gda='git diff HEAD'
__git_complete gda _git_diff
alias gds='git diff --staged'
__git_complete gds _git_diff
alias gi='git init'
__git_complete gi _git_init
alias gl='git log'
__git_complete gl _git_log
alias glg='git log --graph --oneline --decorate --all'
__git_complete glg _git_log
alias gld='git log --pretty=format:"%h %ad %s" --date=short --all'
__git_complete gld _git_log
alias gm='git merge'
__git_complete gm _git_merge
alias gmff='git merge --ff-only'
__git_complete gmff _git_merge
alias gma='git merge --abort'
__git_complete gma _git_merge
alias gmc='git merge --continue'
__git_complete gmc _git_merge
alias gpl='git pull'
__git_complete gpl _git_pull
alias gplr='git pull --rebase'
__git_complete gplr _git_pull
alias gp="git push"
__git_complete gp _git_push
alias gpoh='git push origin HEAD'
__git_complete gpoh _git_push
alias grb='git rebase'
__git_complete grb _git_rebase
alias grbc='git rebase --continue'
__git_complete grbc _git_rebase
alias grba='git rebase --abort'
__git_complete grba _git_rebase
alias grs='git reset'
__git_complete grs _git_reset
alias gs='git status'
__git_complete gs _git_status
alias gss='git status --short'
__git_complete gss _git_status
alias gst='git stash'
__git_complete gst _git_stash
alias gsta='git stash apply'
__git_complete gsta _git_stash
alias gstd='git stash drop'
__git_complete gstd _git_stash
alias gstl='git stash list'
__git_complete gstl _git_stash
alias gstp='git stash pop'
__git_complete gstp _git_stash
alias gsts='git stash save'
__git_complete gsts _git_stash

# ----------------------
# Git Functions
# ----------------------
# Git log find by commit message
function glf() { git log --all --grep="$1"; }
```

From the above, the ones I mostly use are:
- `gs` (`git status`),
- `gd` (`git diff`), 
- `gds` (`git diff --staged`), 
- `gaa` (`git add .`), 
- `gcm` (`git commit --message`), 
- `gpoh` (`git push origin HEAD`), 
- `grb` (`git rebase`), 
- `grbc` (`git rebase --continue`), 
- `grba` (`git rebase --abort`), 
- `gcob` (`git checkout --branch`), and
- `gld` (`git log --pretty=format:"%h %ad %s" --date=short --all`).


## Gnome

Gnome has an excellent [extension system](https://extensions.gnome.org/) which provides some excellent extensions. Here's a couple I use.

### Gnome workspaces

This is actually not an extension but a part of the base Gnome system. It allows you to have windows in multiple workspaces, between which you can move using a keyboard or a mouse. I use 4 workspaces in one row and move between them using shortcuts `CTRL+ALT+H`/`CTRL+ALT+L` to switch to a workspace on the left/right, and `CTRL+SHIFT+ALT+H/L` to move a window to a workspace on the left/right. I usually use the first workspace to host IDEs and terminals, the second to host Firefox and Slack, and the other two for various less-accessed programs such as KeePass. Using workspaces means in such a way means better organization and fewer pressings of `ALT+TAB`.

### Gtile

[Gtile](https://extensions.gnome.org/extension/28/gtile/) allows for re-positioning of windows within a workspace. Instead of grabbing a mouse and dragging/resizing a window, I set up a numerous Gtile shortcuts that position my windows to the places I most often want them to be. For example, I've set up the shortcuts `CTRL+WIN+U/I/N/M` to move the currently focused window to top-left/top-right/bottom-left/bottom-right quarter of the screen, respectively.

### Impatience

To speed up animations that take place when switching between workflows, I use the extension called [Impatiance](https://extensions.gnome.org/extension/277/impatience/) which makes animations go faster.

### Drop down terminal

The [Drop down terminal](https://extensions.gnome.org/extension/442/drop-down-terminal/) extension displays a quick terminal window on the top of the screen, after pressing `CTRL+ALT+F11`.
