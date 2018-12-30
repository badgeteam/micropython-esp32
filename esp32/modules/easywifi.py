# File: easywifi.py
# Version: 1
# Description: Wrapper that makes using wifi simple
# License: MIT
# Authors: Renze Nicolai <renze@rnplus.nl>

import time, network, badge, easydraw, virtualtimers as vt

state = False
failed = False

connected = False

_connCounter = 0
_cb = None

def status():
    global state
    return state

def failure():
    global failed
    return failed

def force_enable():
    global state
    state = False
    global failed
    failed = False
    enable()
    
def enable_custom(ssid, password, showStatus=True):
	global failed, state, connected
	if not state:
		nw = network.WLAN(network.STA_IF)
		if not nw.isconnected():
			nw.active(True)
			if showStatus:
				easydraw.msg("Connecting to '"+ssid+"'...")
			nw.connect(ssid, password) if password else nw.connect(ssid)
			timeout = badge.nvs_get_u8('badge', 'wifi.timeout', 40)
			while not nw.isconnected():
				time.sleep(0.1)
				timeout = timeout - 1
				if (timeout<1):
					if showStatus:
						easydraw.msg("Error: could not connect!")
					disable()
					failed = True
					return False
			state = True
			connected = True
			failed = False
			if showStatus:
				easydraw.msg("Connected!")
	return True

def _background_task():
	global connected, _cb
	nw = network.WLAN(network.STA_IF)
	new = nw.isconnected()
	if connected != new:
		connected = new
		print("[WIFI] Connection state changed ",connected)
		_cb(connected)
	return 1000

def enable_background_custom(ssid, password, callback=None):
	global failed, state, _connCounter, connected, _cb
	if not state:
		nw = network.WLAN(network.STA_IF)
		if not nw.isconnected():
			state = True
			nw.active(True)
			nw.connect(ssid, password) if password else nw.connect(ssid)
			connected = False
			_connCounter = 0
			_cb = callback
			if _cb != None:
				vt.new(1000, _background_task, True)

def enable_background(callback=None):
	ssid = badge.nvs_get_str('badge', 'wifi.ssid', 'SHA2017-insecure')
	password = badge.nvs_get_str('badge', 'wifi.password')
	enable_background_custom(ssid, password, callback)

def enable(showStatus=True):
	ssid = badge.nvs_get_str('badge', 'wifi.ssid', 'SHA2017-insecure')
	password = badge.nvs_get_str('badge', 'wifi.password')
	return enable_custom(ssid, password, showStatus)

def disable():
	global state
	state = False
	global failed
	failed = False
	nw = network.WLAN(network.STA_IF)
	nw.active(False)
	vt.delete(_background_task)

def ifconfig():
	nw = network.WLAN(network.STA_IF)
	return nw.ifconfig()

def wlan():
	return network.WLAN(network.STA_IF)
