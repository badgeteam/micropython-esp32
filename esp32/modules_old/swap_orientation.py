import badge, appglue

curr = badge.nvs_get_u8('badge', 'orientation', 0)
if curr < 90:
	badge.nvs_set_u8('badge', 'orientation', 90)
else:
	badge.nvs_set_u8('badge', 'orientation', 0)

appglue.home()
