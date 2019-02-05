import ugfx, time, badge, machine, deepsleep, gc
import appglue, virtualtimers
import easydraw, easywifi, easyrtc

import tasks.powermanagement as pm
import tasks.otacheck as otac
import tasks.services as services
import term, term_menu

import orientation

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
		easydraw.nickname()
		if goingToSleep:
			info = 'Sleeping...'
		elif badge.safe_mode():
			info = "(Services disabled!)"
		elif otac.available(False):
			info = 'Update available!'
		else:
			info = ''
		easydraw.disp_string_right_bottom(0, info)

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

def goToSleep():
	onSleep(virtualtimers.idle_time())

def onSleep(idleTime):
	draw(False, True)
	services.force_draw(True)
	draw(True, True)

### PROGRAM

splash_input_init()

# post ota script
import post_ota

orientation.default()

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

umenu = term_menu.UartMenu(goToSleep, pm, badge.safe_mode())
umenu.main()
