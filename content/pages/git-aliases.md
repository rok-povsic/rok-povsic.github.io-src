Title: Git aliases
Authors: Rok Povšič
Status: hidden


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
alias gd='git diff'
__git_complete gd _git_diff
alias gda='git diff HEAD'
__git_complete gda _git_diff
alias gds='git diff --staged'
__git_complete gds _git_diff
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
alias gst='git stash'
__git_complete gst _git_stash
alias gstp='git stash pop'
__git_complete gstp _git_stash
```
