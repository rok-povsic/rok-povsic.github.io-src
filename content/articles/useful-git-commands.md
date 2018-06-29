Title: A list of useful Git commands
Date: 2018-06-29 22:06
Category: git
Tags: git
Authors: Rok Povšič

# Useful Git commands

Here's a list of Git commands that solve specific problems I encounter sometimes. I find these commands very useful, although I don't use them every day, which means I tend to forget them and have to re-search for them. I'm storing them here for easy access. Maybe somebody's going to find them useful too.

## Remove all changes from staging (but keep the actual changes)
```
git reset HEAD -- .
```

## Delete last commit but keep the changes
```
git reset HEAD^
```

## Delete all unstaged changes
```
git clean -df
git checkout -- .
```

## Revert an accidentally executed `git commit --amend`
```
git reset --soft HEAD@{1}
```

## Reset the local branch to be exactly like the remote branch

```
 git fetch origin
 git reset --hard origin/branch_name
```

## Start the modification of the last three commits (for example to rename them) 
```
git rebase -i HEAD~3
```
