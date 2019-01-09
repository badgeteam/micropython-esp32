import badge, easydraw

lvl = badge.nvs_get_u8('ota', 'fixlvl', 0)

if lvl<2:
    badge.nvs_set_u8('ota', 'fixlvl', 2) #For SHA2017 compatibility
