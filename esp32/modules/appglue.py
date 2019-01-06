import ugfx, esp, badge, deepsleep, term, lcd

def start_app(app, display = True):
	if display:
		lcd.fb.fill(0)
		lcd.fb.text("Loading...", 0, 0, 1)
		if app:
			term.header(True, "Loading application "+app+"...")
			lcd.fb.text(app, 0, 10, 1)
		else:
			term.header(True, "Returning to the main menu...")
			lcd.fb.text("Homescreen", 0, 10, 1)
		lcd.write()
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
