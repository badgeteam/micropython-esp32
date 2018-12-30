# File: powermanagement.py
# Version: 2
# Description: Power management task, puts the badge to sleep when idle
# License: MIT
# Authors: Renze Nicolai <renze@rnplus.nl>

import virtualtimers, deepsleep, badge, sys

requestedStandbyTime = 0
onSleepCallback = None

userResponseTime = badge.nvs_get_u16('splash', 'urt', 6000)

disabled = False

def disable():
	disabled = True
	kill()
	
def enable():
	disabled = False
	feed()

def state():
	if disabled:
		return -1
	return userResponseTime

def usb_attached():
	return badge.usb_volt_sense() > 4500

def pm_task():
	''' The power management task [internal function] '''
	global requestedStandbyTime
	global userResponseTime
	
	if disabled:
		return userResponseTime
	
	idleTime = virtualtimers.idle_time()
	
	if idleTime > 30000 and not badge.safe_mode() and not ( usb_attached() and badge.nvs_get_u8('badge', 'usb_stay_awake', 0) != 0 ):
		global onSleepCallback
		if not onSleepCallback==None:
			print("[Power management] Running onSleepCallback...")
			try:
				onSleepCallback(idleTime)
			except BaseException as e:
				print("[ERROR] An error occured in the on sleep callback.")
				sys.print_exception(e)
		deepsleep.start_sleeping(idleTime)
	
	return userResponseTime

def feed():
    ''' Start / resets the power management task '''
    global userResponseTime
    if not virtualtimers.update(userResponseTime, pm_task):
        virtualtimers.new(userResponseTime, pm_task, True)

def kill():
    ''' Kills the power management task '''
    virtualtimers.delete(pm_task)
    
def callback(cb):
    ''' Set a callback which is run before sleeping '''
    global onSleepCallback
    onSleepCallback = cb
    
def set_timeout(t):
    ''' Set timeout '''
    global userResponseTime
    userResponseTime = t
