% Developer Tools—Pareto Style
% Grant Skaggs 
% 19 August 2020

# Developer Tools—Pareto Style

Just like the success of musical composers, professional tennis players, and dominant lobsters, the attention I give my developer tools falls in a steep [Pareto distribution](https://en.wikipedia.org/wiki/Pareto_distribution). Here’s my list of essential commands and utilities I use in almost every programming project.

### Git

An immensely popular version control tool.

Favorite commands:

* `git add .`
* `git commit -m “commit message here”`
* `git pull`
* `git push`
* `git checkout branch-name`
* `git checkout -b new-branch-name`
* `git stash`
* `git log`
* `git status`
* `git merge`
* `git clone`

### Linux

Navigating the command-line like a pro.

[Here](../resources/dev-tools/linux.pdf) is the recommended introduction for UTCS Pod students.

Favorite commands:

* `cd`
* `ls`
* `mkdir`
* `mv`
* `cp`
* `scp`
* `rm`
* `ssh cs-username@carmen.cs.utexas.edu`
* `clear`
* `grep`

### Vim

I have a love-hate relationship with vim. Very useful despite being very ugly. 

[Here](../resources/dev-tools/vim.pdf) is the recommended introduction for UTCS Pod students.

### Oh My Zsh

IMO no terminal is complete until tricked out with [Oh My Zsh.](https://ohmyz.sh/)

Also don't forget to make your life easier by adding some aliases and functions to your `~/.zshrc` Personally, I frequently use the following:

* `alias py="python3"`
* `alias gs='git status'`
* `alias ga='git add'`
* `alias gl='git log'`
* `alias gd='git diff'`
* `alias gc='git commit'`

`ac() {` <br>
    `git add .` <br>
    `git commit -m $1` <br> 
`}`

`acp() {`<br>
    `git add .`<br>
    `git commit -m $1`<br>
    `git push`<br>
`}`