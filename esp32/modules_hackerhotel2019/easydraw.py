import ugfx, badge, version, time

# Functions
def msg_nosplit(message, title = 'Loading...', reset = False):
	"""Show a terminal style loading screen with title

	title can be optionaly set when resetting or first call
	"""
	global messageHistory

	try:
		messageHistory
		if reset:
			raise exception
	except:
		ugfx.clear(ugfx.WHITE)
		ugfx.string(0, 0, title, version.font_header, ugfx.BLACK)
		messageHistory = []

	if len(messageHistory)<3:
		ugfx.string(0, 19 + (len(messageHistory) * 13), message, version.font_default, ugfx.BLACK)
		messageHistory.append(message)
	else:
		messageHistory.pop(0)
		messageHistory.append(message)
		ugfx.area(0, 15, 128, 49, ugfx.WHITE)
		for i, message in enumerate(messageHistory):
			ugfx.string(0, 19 + (i * 13), message, version.font_default, ugfx.BLACK)

	ugfx.flush(ugfx.LUT_FASTER)
	
def msg(message, title = "Loading...", reset = False, wait = 0):
	try:
		lines = lineSplit(str(message))
		for i in range(len(lines)):
			if i > 0:
				msg_nosplit(lines[i])
			else:
				msg_nosplit(lines[i], title, reset)
			if (i > 1) and (wait > 0):
				time.sleep(wait)
	except BaseException as e:
		print("!!! Exception in easydraw.msg !!!")
		print(e)

def nickname(y = 0, font = version.font_nickname_large, color = ugfx.BLACK, lineHeight=15):
	nick = badge.nvs_get_str("owner", "name", 'WELCOME TO DISOBEY')
	lines = lineSplit(nick, ugfx.width(), font)
	for i in range(len(lines)):
		line = lines[len(lines)-i-1]
		pos_x = int((ugfx.width()-ugfx.get_string_width(line, font)) / 2)
		ugfx.string(pos_x, y+lineHeight*(len(lines)-i-1), line, font, color)
	return len(lines) * lineHeight

def battery(on_usb, vBatt, charging):
	pass

def disp_string_right_bottom(y, s):
	l = ugfx.get_string_width(s,version.font_default)
	ugfx.string(ugfx.width()-l, ugfx.height()-(y+1)*14, s, version.font_default,ugfx.BLACK)

def lineSplit(message, width=ugfx.width(), font=version.font_default):
	words = message.split(" ")
	lines = []
	line = ""
	for word in words:
		wordLength = ugfx.get_string_width(word, font)
		lineLength = ugfx.get_string_width(line, font)
		if wordLength > width:
			lines.append(line)
			lines.append(word)
			line = ""
		elif lineLength+wordLength < width:
			if (line==""):
				line = word
			else:
				line += " "+word
		else:
			lines.append(line)
			line = word
	if len(line) > 0:
		lines.append(line)
	return lines
