import ugfx, time, badge, machine, deepsleep, gc
import appglue, virtualtimers
import easydraw, easywifi, easyrtc

import tasks.powermanagement as pm
import tasks.otacheck as otac
import tasks.services as services
import term, term_menu

# Graphics

def draw(mode, goingToSleep=False):
	info1 = ''
	info2 = ''
	if mode:
		# We flush the buffer and wait
		ugfx.flush(ugfx.GREYSCALE)
	else:
		# We prepare the screen refresh
		ugfx.clear(ugfx.WHITE)
		if goingToSleep:
			info1 = 'Sleeping...'
			info2 = ''
		else:
			info1 = 'Welcome!'
			if otac.available(False):
				info2 = 'OTA update available!'
			else:
				info2 = ''

		def disp_string_right(y, s):
			l = ugfx.get_string_width(s,"Roboto_Regular12")
			ugfx.string(ugfx.height()-l, y, s, "Roboto_Regular12",ugfx.BLACK)

		disp_string_right(0, info1)
		disp_string_right(12, info2)

		if badge.safe_mode():
			disp_string_right(24, "Safe mode")

		easydraw.nickname()

# Button input

def splash_input_start(pressed):
	# Pressing start always starts the launcher
	if pressed:
		appglue.start_app("launcher", False)

def splash_input_other(pressed):
	if pressed:
		pm.feed()

def splash_input_init():
	print("[SPLASH] Inputs attached")
	ugfx.input_init()
	ugfx.input_attach(ugfx.BTN_START, splash_input_start)
	ugfx.input_attach(ugfx.BTN_B, splash_input_other)
	ugfx.input_attach(ugfx.JOY_UP, splash_input_other)
	ugfx.input_attach(ugfx.JOY_DOWN, splash_input_other)
	ugfx.input_attach(ugfx.JOY_LEFT, splash_input_other)
	ugfx.input_attach(ugfx.JOY_RIGHT, splash_input_other)

# Power management

def onSleep(idleTime):
	draw(False, True)
	services.force_draw(True)
	draw(True, True)

### PROGRAM

splash_input_init()

# post ota script
import post_ota

setupState = badge.nvs_get_u8('badge', 'setup.state', 0)
if setupState < 3: #First boot (3 for SHA compat)
	print("[SPLASH] Force ota check...")
	badge.nvs_set_u8('badge', 'setup.state', 3)
	if not easywifi.failure():
		otac.available(True)
else: # Normal boot
	print("[SPLASH] Normal boot... ("+str(machine.reset_cause())+")")
	if (machine.reset_cause() != machine.DEEPSLEEP_RESET):
		print("... from reset: checking for ota update")
		if not easywifi.failure():
			otac.available(True)

# RTC ===
#if time.time() < 1482192000:
#	easyrtc.configure()
# =======

if badge.safe_mode():
	draw(False)
	services.force_draw()
	draw(True)
else:
	have_services = services.setup(draw) # Start services
	if not have_services:
		draw(False)
		services.force_draw()
		draw(True)

easywifi.disable()
gc.collect()

virtualtimers.activate(25)
pm.callback(onSleep)
pm.feed()

badge.backlight(255)

umenu = term_menu.UartMenu(onSleep, badge.safe_mode())
umenu.main()
