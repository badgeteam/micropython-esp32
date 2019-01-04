import ugfx, badge, version, helpers.term as term

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


def message(content, title = "Loading...", reset=False):
	"""
	Show a terminal style loading screen with title
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
		term.header(True, title)
		messageHistory = []
	print(content)
	if len(messageHistory)<version.message_max_lines:
		messageHistory.append(content)
		ugfx.string(0, 30 + (len(messageHistory) * 15), content, version.font_default, ugfx.BLACK)
	else:
		messageHistory.pop(0)
		messageHistory.append(content)
		ugfx.area(0,30, 296, 98, ugfx.WHITE)
		for i, message in enumerate(messageHistory):
			ugfx.string(0, 30 + (i * 15), message, version.font_default, ugfx.BLACK)

def nickname(y = 25, font = version.font_nickname_large, color = ugfx.BLACK, split = version.nick_width_large, height = version.nick_height_large):
	nick = badge.nvs_get_str("owner", "name", 'Henk de Vries')
	if ugfx.orientation() != 0:
		split = version.nick_width_small
		if font == version.font_nickname_large:
			font = version.font_nickname_small
			height = version.nick_height_small
		lines = lineSplit(nick, split)
		print("Nickname",split,font,lines,y,height)
		for i in range(0, len(lines)):
			print("string_box",0, y+height*i, ugfx.width(), height, lines[i], font, color, ugfx.justifyCenter)
			ugfx.string_box(0, y+height*i, ugfx.width(), height, lines[i], font, color, ugfx.justifyCenter)
	else:
		ugfx.string_box(0, y, ugfx.width(), height, nick, font, color, ugfx.justifyCenter)

def battery(on_usb, vBatt, charging):
    vMin = badge.nvs_get_u16('batt', 'vmin', 3500) # mV
    vMax = badge.nvs_get_u16('batt', 'vmax', 4100) # mV
    if charging and on_usb:
        try:
            badge.eink_png(0,0,'/lib/resources/chrg.png')
        except:
            ugfx.string(0, 0, "CHRG",'Roboto_Regular12',ugfx.BLACK)
    elif on_usb:
        try:
            badge.eink_png(0,0,'/lib/resources/usb.png')
        except:
            ugfx.string(0, 0, "USB",'Roboto_Regular12',ugfx.BLACK)
    else:
        width = round((vBatt-vMin) / (vMax-vMin) * 44)
        if width < 0:
            width = 0
        elif width > 38:
            width = 38
        ugfx.box(2,2,46,18,ugfx.BLACK)
        ugfx.box(48,7,2,8,ugfx.BLACK)
        ugfx.area(3,3,width,16,ugfx.BLACK)
