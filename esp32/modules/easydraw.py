# File: easydraw.py
# Description: Wrapper that makes drawing things simple
# License: MIT
# Authors: Renze Nicolai <renze@rnplus.nl>

import ugfx, badge, version, disobey

# Functions
def msg(message, title = 'Loading...', reset = False):
    """Show a terminal style loading screen with title

    title can be optionaly set when resetting or first call
    """
    global messageHistory

    try:
        messageHistory
        if reset:
            raise exception
    except:
        disobey.lcd.clear()
        disobey.fb.text(title, 0, 0, 1)
        messageHistory = []

    disobey.fb.text(message, 0, 10, 1)

    disobey.fb_write()

def nickname(y = 25, font = version.font_nickname_large, color = ugfx.BLACK, split = version.nick_width_large, height = version.nick_height_large):
	nick = badge.nvs_get_str("owner", "name", 'Henk de Vries')
	disobey.fb.text(nick, 0, 54, 1)

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
