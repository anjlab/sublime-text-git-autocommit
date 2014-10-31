Why auto-committing anything at all?
====================================

I like using Sublime Text as a buffer for:

 * working with text from clipboard,
 * or writing random notes in the way only I can understand

Such notes usually change a lot during a day, and I often need to find a piece of text I had in there.

This little plugin automatically tracks history of such notes. It stores the history in a Git repo.


How it works?
=============

Commit happens when you either:
 * save any file from your Git repo manually,
 * or with a 30 seconds delay when you made any change to the files.

Every changed file added & committed separately with commit message like:
> Auto-committing 'TODO.txt'


How to use?
===========

 1. Create new Git repository for your temporary files

  ```
mkdir ~/Documents/Notes
cd ~/Documents/Notes
git init
```
 2. Add empty file with name `.sublime-text-git-autocommit` to the root folder to activate this plugin

  ```
touch .sublime-text-git-autocommit
git commit -am "Commit .sublime-text-git-autocommit"
```
 3. Create one or more text files at the same folder and make your notes in there

  ```
touch TODO
touch Clipboard
```
 4. All changes made via Sublime to these files will be committed automatically (nested folders ignored)

How to view history?
====================

Use `git log -p`.

Or publish your repo as GitHub Gist and use its diff viewer.

## To publish as GitHub Gist:
 1. Create [new private Gist](https://gist.github.com)
 2. Copy git clone URL
 3. From the root folder of your git repo

  ```
git remote add origin https://gist.github.com/YOUR_GIST_ID_HERE.git
git remote -v
git branch --set-upstream-to=origin/master master
git pull
```
 4. Push your changes to Gist manually from time-to-time
  
  "Shift+CMD+P" -> type "Git Push" -> Enter
 5. View diffs on GitHub

## GitHub 2FA
If you enabled GitHub's 2-Factor Authentication then you need to use access token to push to your Gist repo from command line.
I found [Gist Tool](https://github.com/defunkt/gist) helpful for this purpose.
```
brew install gist
gist --login
cat ~/.gist
```
Once you have your access token use it as a username when GitHub asks for credentials, leave password empty.


Installation
============

This plugin depends on this beautiful [Git Sublime Text Plugin](https://github.com/kemayo/sublime-text-git), so you should install it first.

It's recommended that you install it via [Package Control](https://github.com/kemayo/sublime-text-git#package-control).

You can also find this plugin in Package Control by the name "GitAutoCommit".


License
=======
[MIT-License](https://raw.githubusercontent.com/anjlab/sublime-text-git-autocommit/master/LICENSE)


How to contribute?
==================
1. Fork it
2. Create your feature branch (git checkout -b my-new-feature)
3. Commit your changes (git commit -am 'Add some feature')
4. Push to the branch (git push origin my-new-feature)
5. Create New Pull Request
