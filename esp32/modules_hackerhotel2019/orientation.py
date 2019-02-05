import badge, version, ugfx

default_orientation = 90 #For hackerhotel badge

def default():
	ugfx.orientation(badge.nvs_get_u8('badge', 'orientation', default_orientation))

def sha2017():
	ugfx.orientation(0)

def disobey2019():
	ugfx.orientation(0)

def hackerhotel2019():
	ugfx.orientation(90)
