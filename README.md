Installation
============

 0. [Install Package Control](https://packagecontrol.io/installation) if you don't have it yet
 1. Install `Git` plugin (required)

  ```
Shift+CMD+P -> Install Package -> Git
```

 2. Install `GitAutoCommit`

  ```
Shift+CMD+P -> Install Package -> GitAutoCommit
```

Why auto-committing anything at all?
====================================

I like using Sublime Text as a buffer for:

 * working with text from clipboard,
 * or writing random notes in the way only I can understand

Such notes usually change a lot during a day, and I often need to find a piece of text I had in there.

This little plugin helps tracking a history of such notes automatically. It stores the history in a Git repo.


How it works?
=============

You create new Git repo for your notes with an empty file `.sublime-text-git-autocommit`.
This way plugin knows that it should enable auto-commits for files in this repo.

Changes committed when you either:
 * saved a file in your Git repo,
 * or after you made changes to the files (in a 30 seconds delay).

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
 3. Create one or more text files at the same folder and make your notes in them

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
