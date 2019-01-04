import badge, helpers.graphics as graphics

# Read current patch level
lvl = badge.nvs_get_u8('ota', 'fixlvl', 0)

if lvl<2:
    #graphics.message("Running post OTA scripts...","Updating...",)
    badge.nvs_set_u8('ota', 'fixlvl', 2)
