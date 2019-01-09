import ugfx, badge, version

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
        ugfx.clear(ugfx.WHITE)
        ugfx.string(0, 0, title, version.font_header, ugfx.BLACK)
        messageHistory = []

    if len(messageHistory)<2:
        ugfx.string(0, 19 + (len(messageHistory) * 15), message, version.font_default, ugfx.BLACK)
        messageHistory.append(message)
    else:
        messageHistory.pop(0)
        messageHistory.append(message)
        ugfx.area(0, 15, 128, 49, ugfx.WHITE)
        for i, message in enumerate(messageHistory):
            ugfx.string(0, 19 + (i * 15), message, version.font_default, ugfx.BLACK)

    ugfx.flush(ugfx.LUT_FASTER)

def nickname(y = 0, font = version.font_nickname_large, color = ugfx.BLACK):
    nick = badge.nvs_get_str("owner", "name", 'John Doe')
    ugfx.string_box(0,y,ugfx.width(),15, nick, font, color, ugfx.justifyCenter)

def battery(on_usb, vBatt, charging):
    pass

def disp_string_right_bottom(y, s):
	l = ugfx.get_string_width(s,"Roboto_Regular12")
	ugfx.string(ugfx.width()-l, ugfx.height()-(y+1)*14, s, "Roboto_Regular12",ugfx.BLACK)
