import machine, badge, time

pin = machine.Pin(25)
rtc = machine.RTC()
rtc.wake_on_ext0(pin = pin, level = 0)

def start_sleeping(duration=0):
	badge.backlight(0)
	time.sleep(0.1)
	machine.deepsleep(duration)

def reboot():
	machine.deepsleep(1)
