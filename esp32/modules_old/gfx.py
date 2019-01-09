# Colors
BLACK = 0
WHITE = 1

# Buttons
JOY_UP = 1
JOY_DOWN = 2
JOY_LEFT = 3
JOY_RIGHT = 4
BTN_A = 6
BTN_B = 7
BTN_SELECT = 8
BTN_START = 9
BTN_FLASH = 10

LUT_FULL = 0
LUT_NORMAL = 1
LUT_FASTER = 2
LUT_FASTEST = 3
LUT_MAX = LUT_FASTEST
LUT_DEFAULT = LUT_FULL
GREYSCALE = 255

justifyLeft = 0
justifyCenter = 1
justifyRight = 2

def init():
	pass

def deinit():
	pass

def set_lut(selected_lut):
	pass

def get_lut():
	pass

def clear(color=WHITE):
	pass

def flush(lut=None):
	if not lut == None:
		set_lut(lut)
	pass

def poll():
	pass

def get_string_width(data, font):
	pass

def get_char_width(data, font):
	pass

def char(x0, y0, data, font, col):
	pass

def string(x0, y0, data, font, col):
	pass

def text(x0, y0, data, col):
	pass

def string_box(x0, y0, x1, y1, data, font, col, justify):
	pass

def get_pixel(x_in, y_in):
	pass

def pixel(x0, y0, col):
	pass

def line(x0, y0, x1, y1, col):
	pass

def box(x0, y0, a, b, col):
	pass

def rounded_box(x0, y0, a, b, r, col):
	pass

def fill_rounded_box(x0, y0, a, b, r, col):
	pass

def area(x0, y0, a, b, col):
	pass

def thickline(x0, y0, x1, y1, col, width, rnd):
	pass

def circle(x0, y0, r, col):
	pass

def fill_circle(x0, y0, r, col):
	pass

def ellipse(x0, y0, a, b, col):
	pass

def fill_elipse(x0, y0, a, b, col):
	pass

def arc(x0, y0, r, a1, a2, col):
	pass

def fill_arc(x0, y0, r, a1, a2, col):
	pass

def polygon(x0, y0, arr, col):
	pass

def fill_polygon(x0, y0, arr, col):
	pass

def display_image(x, y, img):
	pass

def orientation(new=None):
	if not new == None:
		pass
	return 0

def width():
	return 0

def height():
	return 0

def fonts_list():
	pass

#def fonts_dump(font):
#	pass

#def fonts_load():
#	pass

def input_init():
	pass

def input_attach(btn, callback):
	pass

def demo():
	pass

def set_default_font(font):
	pass

def set_default_style(style):
	pass

def send_tab():
	pass

class Button:
	def __init__(self):
		pass

class Container:
	def __init__(self):
		pass
	
class Font():
	def __init__(self):
		pass
	
class List():
	def __init__(self):
		pass

class Textbox():
	def __init__(self):
		pass

class Style():
	def __init__(self):
		pass
	
class Keyboard():
	def __init__(self):
		pass
	
class Label():
	def __init__(self):
		pass
	
class Image():
	def __init__(self):
		pass

class Checkbox():
	def __init__(self):
		pass
	
class Imagebox():
	def __init__(self):
		pass
