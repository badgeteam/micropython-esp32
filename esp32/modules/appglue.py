import ugfx, esp, badge, deepsleep, term

def start_app(app, display = True):
	if display:
		ugfx.clear(ugfx.WHITE)
		ugfx.string(0, 0, "Loading...", "PermanentMarker22", ugfx.BLACK)
		if app:
			term.header(True, "Loading application "+app+"...")
			ugfx.string(0,  25, "Starting "+app+"...","Roboto_Regular12",ugfx.BLACK)
		else:
			term.header(True, "Returning to the main menu...")
			ugfx.string(0,  25, "Returning to homescreen...","Roboto_Regular12",ugfx.BLACK)
		ugfx.flush(ugfx.LUT_FASTER)
	esp.rtcmem_write_string(app)
	deepsleep.reboot()

def home():
	start_app("")

def start_ota():
	term.header(True, "Starting OTA...")
	esp.rtcmem_write(0,1)
	esp.rtcmem_write(1,254)
	deepsleep.reboot()

def start_bpp(duration):
	term.header(True, "Starting BPP...")
	print("[BPP] Duration = "+str(duration))
	esp.rtcmem_write(0,2)
	esp.rtcmem_write(1,253)
	deepsleep.reboot()

def debug_factory():
	badge.nvs_set_u8('sponsors', 'shown', 0)
	badge.nvs_set_u8('ota', 'fixlvl', 0)
	badge.nvs_set_u8('badge', 'setup.state', 0)
	start_app("")
