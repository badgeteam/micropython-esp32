# File: splash.py
# Description: App launcher & homescreen
# License: MIT
# Author: Renze Nicolai <renze@rnplus.nl>

import ugfx, time, badge, machine, gc, sys
import appglue as app
import virtualtimers as vt
import easydraw as draw
import easywifi as wifi
import easyrtc as rtc
import tasks.powermanagement as pm
import tasks.otacheck as otac
import tasks.resourcescheck as resc
import tasks.sponsorscheck as spoc
import tasks.services as services
import term
import deepsleep as ds
import version
import orientation
import term_menu
import disobey

class Splash:
	redraw = True
	selected = 0
	
	def __init__(self):
		print("[SPLASH] init")
		self.umenu = term_menu.UartMenu(self, badge.safe_mode())
			
	def leds_off(self):
		for i in range(6):
			disobey.dev.led(i,0,0,0)
	
	def wait_for_buttons(self):
		while (disobey.dev.read_buttons() > 0):
			pm.feed()
			time.sleep(0.01)
	
	def task_main(self):
		if self.redraw:
			self.screen_main()
			self.redraw = False
		i = disobey.dev.read_buttons()
		if i > 0:
			pm.feed()
		if i == (1<<disobey.dev.BTN_OK): #OK button
			self.wait_for_buttons()
			services.stop()
			self.leds_off()
			self.menu_main()
			return -1
		return 100
	
	def touch_flush(self):
		pass
	
	def home(self):
		self.redraw = True
		self.touch_flush()
		vt.delete(self.task_main)
		vt.new(1, self.task_main, True)
		services.setDrawCallback(self.screen_main)
		services.start()
		pm.feed()
		
	def go_to_sleep(self):
		self.on_sleep(86400000)
		
	def opt_change_nickname(self):
		app.start_app("setup")
	
	def opt_launcher(self):
		app.start_app("launcher")
	
	def opt_configure_wifi(self):
		app.start_app("wifi")
		
	def opt_ota(self):
		app.start_ota()
	
	def opt_update_apps(self):
		app.start_app("update")
		
	def opt_about(self):
		app.start_app("about")
		
	def opt_swap_orientation(self):
		app.start_app("swap_orientation")
		
	def menu_draw(self, title, items, selected):
		disobey.fb.fill(0)
		disobey.fb.text(title, 0, 0, 1)
		disobey.fb.text("---------", 0, 10, 1)
		y = 2
		for i in range(0, len(items)):
			text = "  "+items[i]
			if selected == i:
				text = "> "+items[i]
			disobey.fb.text(text, 0, 10*y, 1)
			y += 1
		disobey.fb_write()
		
		
	def menu_task(self):
		i = disobey.dev.read_buttons()
		if i > 0:
			pm.feed()
			self.wait_for_buttons()
		if i == (1<<disobey.dev.BTN_UP): #Up
			if (self.menu_selected>0):
				self.menu_selected -= 1
				self.redraw = True
		if i == (1<<disobey.dev.BTN_DOWN): #Down
			if (self.menu_selected<len(self.menu_items)-1):
				self.menu_selected += 1
				self.redraw = True
		if i == (1<<disobey.dev.BTN_OK): #OK
			self.menu_callbacks[self.menu_selected]()
			return -1
		if i == (1<<disobey.dev.BTN_BACK): #B
			self.menu_callbacks[len(self.menu_callbacks)-1]() #Run last callback
			return -1
		if self.redraw:
			self.menu_draw(self.menu_title, self.menu_items, self.menu_selected)
			self.redraw = False
		return 100
		
	def menu(self, title, items, callbacks):
		self.redraw = True
		self.touch_flush()
		self.menu_items = items
		self.menu_callbacks = callbacks
		self.menu_selected = 0
		self.menu_title = title
		vt.delete(self.menu_task)
		vt.new(1, self.menu_task, True)

	def menu_settings(self):
		items = ["Change nickname", "Configure WiFi", "OTA update", "Update all apps", "< Return to main menu"]
		callbacks = [self.opt_change_nickname, self.opt_configure_wifi, self.opt_ota, self.opt_update_apps,  self.menu_main, self.menu_main]
		self.menu("Settings", items, callbacks)
		
	def menu_main(self):
		items = ["Apps", "Settings", "About", "Power off"]
		callbacks = [self.opt_launcher, self.menu_settings, self.opt_about, self.go_to_sleep, self.home]
		self.menu("Main menu", items, callbacks)
		
	def menu_recovery(self):
		items = ["Apps", "Change nickname", "Configure WiFi", "OTA update", "Update all apps", "Power off"]
		callbacks = [self.opt_launcher, self.opt_change_nickname, self.opt_configure_wifi, self.opt_ota, self.opt_update_apps, self.go_to_sleep, self.menu_recovery]
		self.menu("Recovery menu", items, callbacks)
	
	def screen_main(self, init=False):
		# Homescreen for normally booted badges
		disobey.fb.fill(0)
		draw.nickname(0)
		disobey.fb.text("Welcome!",0,0,1)
		if not init:
			disobey.fb_write()
	
	def on_sleep(self, idleTime):
		# Executed before the badge goes to sleep
		disobey.dev.backlight(0)
		disobey.fb.fill(0)
		draw.nickname(0)
		services.force_draw()
		services.stop()
		self.leds_off()
		disobey.fb_write()
		ds.start_sleeping(idleTime) #Seems double (pm does this as well) but needed for uart menu
	
	def main(self):
		disobey.dev.backlight(255)
		print("[SPLASH] main")
		orientation.default()
		safe = badge.safe_mode()
		print("[SPLASH] Safe mode? ", safe)
		vt.activate(25)
		
		self.redraw = True
		
		if not safe:
			pm.callback(self.on_sleep)
			services.setup()
			pm.enable()
			self.home()
		else:
			pm.disable()
			self.menu_recovery()
		
		self.umenu.main() # Jump to the serial port menu application


print("[MAIN] Welcome!")
splash = Splash()
splash.main()
print("[MAIN] --- Application terminated ---")
