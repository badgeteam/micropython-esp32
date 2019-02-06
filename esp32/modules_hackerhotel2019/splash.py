import ugfx, time, badge, machine, deepsleep, gc
import appglue, virtualtimers
import easydraw, wifi, rtc

import tasks.powermanagement as pm

import term, term_menu

import orientation

if badge.safe_mode():
	print("Safe-mode: jump to launcher on boot!")
	appglue.start_app("launcher", False)

oldWifiStatus = False
wifiStatus = False
redraw = True

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
	global redraw
	redraw = True
	drawTask(True)
	print("SLEEPING FOR",idleTime)
	deepsleep.start_sleeping(idleTime)

### PROGRAM

splash_input_init()

# post ota script
import post_ota

# Sponsors
if not badge.nvs_get_u8('sponsors', 'shown', 0):
	badge.nvs_set_u8('sponsors', 'shown', 1)
	appglue.start_app("sponsors")

orientation.default()

gc.collect()

virtualtimers.activate(25)
pm.callback(onSleep)
pm.feed()

if not rtc.isSet():
	wifi.connect()

def wifiStatusTask():
	global oldWifiStatus, wifiStatus, redraw
	oldWifiStatus = wifiStatus
	wifiStatus = wifi.status()
	if wifiStatus:
		wifi.ntp(True)
	if wifiStatus != oldWifiStatus:
		oldWifiStatus = wifiStatus
		redraw = True
	return 1000

virtualtimers.new(10, wifiStatusTask, True)

def drawTask(onSleep=False):
	global redraw
	if redraw:
		redraw = False
		ugfx.clear(ugfx.WHITE)
		easydraw.nickname()
		#services.draw()
		info = 'Welcome!'
		if onSleep:
			info = 'Sleeping...'
		elif badge.safe_mode():
			info = "Recovery mode"
		elif not rtc.isSet():
			info = "Clock not set"
		elif wifiStatus:
			info = "WiFi connected"
		ugfx.line(0, ugfx.height()-15, ugfx.width(), ugfx.height()-15, ugfx.BLACK)
		easydraw.disp_string_right_bottom(0, info)
		#ugfx.flush(ugfx.GREYSCALE)
		ugfx.flush(ugfx.LUT_NORMAL)
	return 1000

virtualtimers.new(10, drawTask, True)


mode = badge.nvs_get_u8('badge', 'splashMode', 1)

if mode == 1:
	umenu = term_menu.UartMenu(goToSleep, pm, badge.safe_mode())
	umenu.main()
elif mode == 2:
	appglue.start_app("shell", False)
elif mode == 3:
	appglue.start_app("launcher", False)
