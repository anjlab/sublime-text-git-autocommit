Why auto-committing anything at all?
====================================

I like using Sublime Text to edit "temporary" files.

For example:

 * a TODO list, which looks like a random notes written in the way only I can understand
 * a text buffer to paste/edit/replace content from clipboard
 * etc.

Such files usually change a lot during a day, but it's often happen that I need to find a piece of text I had in there some time ago.

So I decided to create this little Sublime plugin that would automatically track history for such changes.

And Git seems reasonable version control tool for that.


How it works?
=============

1. Create brand new Git repository for your temporary files
2. Add empty file with name `.sublime-text-git-autocommit` to the root folder
3. All changes made to files in this folder will be auto-committed (nested folders ignored)

Commit happens automatically when you:
 * save the file manually
 * or after 30 seconds delay since your latest change to the file.

Every changed file added & committed separately with commit message like:
> "Auto-committing 'TODO.txt'"

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
