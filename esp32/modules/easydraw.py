# File: easydraw.py
# Description: Wrapper that makes drawing things simple
# License: MIT
# Authors: Renze Nicolai <renze@rnplus.nl>

import badge
import version
import disobey

def msg(message, title = 'Loading...', reset = False):
	disobey.fb.fill(0)
	disobey.fb.text(title, 0, 0, 1)
	disobey.fb.text(message, 0, 10, 1)
	disobey.fb_write()

def nickname(y = 25, font = 0, color = 0, split = version.nick_width_large, height = version.nick_height_large):
	nick = badge.nvs_get_str("owner", "name", 'Henk de Vries')
	disobey.fb.text(nick, 0, 54, 1)

def battery(on_usb, vBatt, charging):
	pass

def lineSplit(message, width):
	words = message.split(" ")
	lines = []
	line = ""
	for word in words:
		if len(word) > width:
			lines.append(line)
			lines.append(word)
			line = ""
		elif len(line)+len(word) < width:
			line += " "+word
		else:
			lines.append(line)
			line = word
	if len(line) > 0:
		lines.append(line)
	return lines
