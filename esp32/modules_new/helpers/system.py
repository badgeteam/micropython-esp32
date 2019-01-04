# This file makes basic system functions available to apps
# It replaces imports like appglue, easywifi, easydraw and deepsleep

import badge, esp, machine, helpers.term as term, version, ugfx, time, helpers.graphics as graphics

def sleep(sleepFor=0, touchWakeup=True):
	"""
	Make the badge go into deep sleep (low power) mode
	Time can be set from one millisecond to one day
	Setting the time parameter to 0 makes the badge sleep forever
	"""
	if touchWakeup:
		pin = machine.Pin(25)
		rtc = machine.RTC()
		rtc.wake_on_ext0(pin = pin, level = 0)
	if (sleepTime >= 86400000): #If sleeping for more than one day
		sleepTime = 0 #Sleep forever
	term.header(True, "Zzz...")
	if (sleepTime < 1):
		print("Sleeping until touchbutton is pressed...")
	else:
		print("Sleeping for "+str(sleepTime)+"ms...")
	badge.eink_busy_wait()
	time.sleep(0.1)
	machine.deepsleep(sleepTime)

def reboot():
	"""
	Reboots the badge without modifying the RTC memory
	This means that the badge will restart the app that calls this function unless
	the app manually sets new boot parameters using esp.rtcmem_write(_string)
	"""
	badge.eink_busy_wait()
	machine.deepsleep(1)
	
def start(app, display=True):
	"""
	Start an app by rebooting the badge and then importing the application file
	"""
	if display:
		if app:
			graphics.message("Loading application "+app+"...")
		else:
			graphics.message("Returning to the main menu...")
	esp.rtcmem_write_string(app)
	reboot()
	
def home(display=True):
	"""
	Reboots the badge and starts the main menu
	"""
	start("",display)

def ota(display=True):
	"""
	Reboots the badge into OTA update mode
	"""
	if display:
		graphics.message("Starting OTA update...")
	esp.rtcmem_write(0,1)
	esp.rtcmem_write(1,254)
	reboot()

def bpp(duration, display=True):
	"""
	Reboots the badge into BPP mode
	"""
	if display:
		graphics.message("Starting BPP ("+str(duration)+")...")
	esp.rtcmem_write(0,2)
	esp.rtcmem_write(1,253)
	reboot()

def factoryReset(display=True):
	"""
	Resets configuration and restarts badge
	"""
	if display:
		graphics.message("Factory reset...")
	esp.rtcmem_write_string("")
	#to-do: add function to format nvs partition
	badge.nvs_set_u8('sponsors', 'shown', 0)
	badge.nvs_set_u8('ota', 'fixlvl', 0)
	badge.nvs_set_u8('badge', 'setup.state', 0)
	reboot()
