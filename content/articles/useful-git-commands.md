Title: A list of useful Git commands
Date: 2018-06-29 22:06
Category: git
Tags: git
Authors: Rok Povšič

Here's a list of Git commands that solve specific problems I encounter sometimes. I find these commands very useful, although I may not use them every day, which means I will tend to forget them and have to re-find them again and again. I'm storing them here for easy access. Maybe somebody's going to find them useful too.

<!-- PELICAN_END_SUMMARY -->

## Remove all changes from staging (but keep the actual changes)
```python
git reset HEAD -- .
```

## Delete last commit but keep the changes
```python
git reset HEAD^
```

## Delete all unstaged changes
```python
git clean -df
git checkout -- .
```

## Revert an accidentally executed `git commit --amend`
```python
git reset --soft HEAD@{1}
```

## Reset the local branch to be exactly like the remote branch

```python
 git fetch origin
 git reset --hard origin/branch_name
```

## Start the modification of the last three commits (for example to rename them) 
```python
git rebase -i HEAD~3
```
