import badge, version, ugfx

def default():
	ugfx.orientation(badge.nvs_get_u8('badge', 'orientation', version.default_orientation))
	
def sha():
	ugfx.orientation(0)

def hackerhotel():
	ugfx.orientation(90)
