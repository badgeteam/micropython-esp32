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
import lcd

class Splash:
	redraw = True
	selected = 0
	
	def __init__(self):
		print("[SPLASH] init")
		self.umenu = term_menu.UartMenu(self, badge.safe_mode())
			
	def leds_off(self):
		for i in range(6):
			badge.led(i,0,0,0)
	
	def touch_interrupt_clear(self):
		ugfx.input_attach(ugfx.JOY_UP, self.touch_interrupt_dummy)
		ugfx.input_attach(ugfx.JOY_DOWN, self.touch_interrupt_dummy)
		ugfx.input_attach(ugfx.JOY_LEFT, self.touch_interrupt_dummy)
		ugfx.input_attach(ugfx.JOY_RIGHT, self.touch_interrupt_dummy)
		ugfx.input_attach(ugfx.BTN_B, self.touch_interrupt_dummy)
		ugfx.input_attach(ugfx.BTN_START, self.touch_interrupt_dummy)
		
	
	def touch_interrupt_dummy(self, pressed):
		print(":D")
		pm.feed()
	
	def main_btn_start(self, pressed):
		pm.feed()
		if pressed:
			self.touch_interrupt_clear()
			services.stop()
			self.leds_off()
			self.menu_main()
	
	def task_main(self):
		if self.redraw:
			self.screen_main()
			self.redraw = False
			return -1
		return 100
	
	def home(self):
		self.redraw = True
		vt.delete(self.task_main)
		vt.new(1, self.task_main, True)
		self.touch_interrupt_clear()
		ugfx.input_attach(ugfx.BTN_START, self.main_btn_start)
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
		lcd.fb.fill(0)
		lcd.fb.text(title, 0, 0, 1)
		lcd.fb.text("---------", 0, 10, 1)
		y = 2
		for i in range(0, len(items)):
			text = "  "+items[i]
			if selected == i:
				text = "> "+items[i]
			lcd.fb.text(text, 0, 10*y, 1)
			y += 1
		lcd.write()
		
	def menu_btn_up(self, pressed):
		pm.feed()
		if pressed:
			if (self.menu_selected>0):
				self.menu_selected -= 1
				self.redraw = True
	
	def menu_btn_down(self, pressed):
		pm.feed()
		if pressed:
			if (self.menu_selected<len(self.menu_items)-1):
				self.menu_selected += 1
				self.redraw = True
	
	def menu_btn_start(self, pressed):
		pm.feed()
		if pressed:
			vt.delete(menu_task)
			self.touch_interrupt_clear()
			self.menu_callbacks[self.menu_selected]()
	
	def menu_btn_back(self, pressed):
		pm.feed()
		if pressed:
			vt.delete(menu_task)
			self.touch_interrupt_clear()
			self.menu_callbacks[len(self.menu_callbacks)-1]()
		
	def menu_task(self):
		if self.redraw:
			self.menu_draw(self.menu_title, self.menu_items, self.menu_selected)
			self.redraw = False
		return 100
		
	def menu(self, title, items, callbacks):
		self.redraw = True
		self.menu_items = items
		self.menu_callbacks = callbacks
		self.menu_selected = 0
		self.menu_title = title
		vt.delete(self.menu_task)
		vt.new(1, self.menu_task, True)
		self.touch_interrupt_clear()
		ugfx.input_attach(ugfx.JOY_UP, self.menu_btn_up)
		ugfx.input_attach(ugfx.JOY_DOWN, self.menu_btn_down)
		ugfx.input_attach(ugfx.BTN_B, self.menu_btn_b)
		ugfx.input_attach(ugfx.BTN_START, self.menu_btn_start)

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
		lcd.fb.fill(0)
		draw.nickname(0)
		lcd.fb.text("Welcome!",0,0,1)
		if not init:
			lcd.write()
	
	def on_sleep(self, idleTime):
		# Executed before the badge goes to sleep
		badge.backlight(0)
		lcd.fb.fill(0)
		draw.nickname(0)
		services.force_draw()
		services.stop()
		self.leds_off()
		lcd.write()
		ds.start_sleeping(idleTime) #Seems double (pm does this as well) but needed for uart menu
	
	def main(self):
		ugfx.input_init()
		badge.backlight(255)
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
