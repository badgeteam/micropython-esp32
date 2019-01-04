import ugfx, time, badge, machine, deepsleep, gc

import tasks.powermanagement as pm
import tasks.otacheck as otac
import tasks.resourcescheck as resc
import tasks.sponsorscheck as spoc
import helpers.system as system, helpers.wifi as wifi

setupState = badge.nvs_get_u8('badge', 'setup.state', 0)
if setupState < 2: #First boot
	print("First boot (show sponsors)...")
	badge.nvs_set_u8('badge', 'setup.state', 2)
	spoc.show(True)
elif setupState == 2: # Third boot: force OTA check
	print("Second boot (force ota check)...")
	badge.nvs_set_u8('badge', 'setup.state', 3)
	if wifi.enable():
		otac.available(True)
	import splash
else:
	print("Normal boot triggered firstboot.py !!! BUG !!!")
