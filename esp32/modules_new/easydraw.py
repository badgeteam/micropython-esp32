import helpers.graphics as graphics, version, ugfx

def msg(message, title = 'Loading...', reset = False):
	graphics.message(message, title, reset)

def nickname(y = 25, font = version.font_nickname_large, color = ugfx.BLACK, split = version.nick_width_large, height = version.nick_height_large):
	graphics.nickname(y, font, color, split, height)

def battery(on_usb, vBatt, charging):
	graphics.battery(on_usb, vBatt, charging)
