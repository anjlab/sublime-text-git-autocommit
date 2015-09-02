import functools
import tempfile
import os
from threading import Timer

import sublime
import sublime_plugin

import Git.git
import Git.add

def AutoCommitFileExists(root, parent = ""):
	if root == parent:
		return False
	marker_file = root + "/.sublime-text-git-autocommit"
	print marker_file
	if not os.path.exists(marker_file):
		return AutoCommitFileExists(os.path.dirname(root), root)
	else:
		return True
	
def is_file_from_autocommit_list(view):
	# Right now all files from folder with special "marker"-file considered to be auto-committed
	# TODO: Maybe put a list of auto-committed files to the "marker"-file? One filename per line
	return AutoCommitFileExists(os.path.realpath(os.path.dirname(view.file_name())))

'''
Inspired by:
https://github.com/kemayo/sublime-text-git
'''
class SilentAddWithCommitCommand(Git.git.GitTextCommand):

	def __init__(self, view):
		self.view = view

	def run(self, edit):
		if not is_file_from_autocommit_list(self.view):
			return

		self.run_command(['git', 'add', self.get_file_name()],
	 		functools.partial(self.add_done, "Auto-committing \'" + os.path.basename(self.get_file_name()) + "\'"))

	def add_done(self, message, result):
		if result.strip():
			sublime.error_message("Error adding file:\n" + result)
			return

		self.run_command(['git', 'commit', '-m', message],
			callback=self.update_status)

	def update_status(self, output, **kwargs):
		sublime.status_message(output)


'''
Inspired by:
https://github.com/jamesfzhang/auto-save
'''
class AutoCommitListener(sublime_plugin.EventListener):

	save_queue = [] # Save queue for on_modified events.

	def on_modified(self, view):
		if not is_file_from_autocommit_list(view):
			return

		# auto-commit on_modified after...
		delay = 30 # seconds

		'''
		Must use this callback for ST2 compatibility
		'''
		def callback():
			view.run_command("silent_add_with_commit")

		'''
		If the queue is longer than 1, pop the last item off,
		Otherwise save and reset the queue.
		'''
		def debounce_save():
			if len(self.save_queue) > 1:
				self.save_queue.pop()
			elif len(self.save_queue) == 0:
				return
			else:
				sublime.set_timeout(callback, 0)
				self.save_queue = []

		if view.file_name():
			self.save_queue.append(0) # Append to queue for every on_modified event.
			Timer(delay, debounce_save).start() # Debounce save by the specified delay.


	def on_post_save(self, view):
		if not is_file_from_autocommit_list(view):
			return

		view.run_command("silent_add_with_commit")
		self.save_queue = []
