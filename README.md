Why auto-committing anything at all?
====================================

I like using Sublime Text to edit "temporary" files.

For example:

 * a buffer to paste/edit/replace text content from clipboard
 * a random notes written in the way only I can understand
 * etc.

Such files usually change a lot during a day.

And it's often happen that I need to find a piece of text I had in there some time ago.

So I decided to create this little Sublime plugin that would automatically track history for such changes.

And Git seems like reasonable version control tool for that.


How to use?
===========

 1. Create new Git repository for your temporary files

  ```
mkdir ~/Documents/TODOs
cd ~/Documents/TODOs
git init
```
 2. Add empty file with name `.sublime-text-git-autocommit` to the root folder to activate this plugin

  ```
touch .sublime-text-git-autocommit
git commit -am "Commit .sublime-text-git-autocommit"
```
 3. All changes made via Sublime to files in this folder will be auto-committed (nested folders ignored)

Commit happens automatically when you either:
 * save the file manually,
 * or after 30 seconds delay since your latest change to the file.

Every changed file added & committed separately with commit message like:
> Auto-committing 'TODO.txt'

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


How to contribute?
==================
1. Fork it
2. Create your feature branch (git checkout -b my-new-feature)
3. Commit your changes (git commit -am 'Add some feature')
4. Push to the branch (git push origin my-new-feature)
5. Create New Pull Request

License
=======
[MIT-License](https://raw.githubusercontent.com/anjlab/sublime-text-git-autocommit/master/LICENSE)
