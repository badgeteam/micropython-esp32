from machine import I2C
from machine import Pin
import ERC12864
import framebuf

class Samd():
	ADDR = 48
	CMD_LED = 0x01
	CMD_BACKLIGHT = 0x02
	CMD_BUZZER = 0x03
	CMD_OFF = 0x04
	
	BTN_LEFT = 0
	BTN_RIGHT = 5
	BTN_UP = 1
	BTN_DOWN = 4
	BTN_BACK = 2
	BTN_OK = 3
	
	def __init__(self, i2c):
		self.i2c = i2c
	
	def backlight(self, brightness):
		self.i2c.writeto(self.ADDR, bytes([self.CMD_BACKLIGHT, brightness&0xFF]))
	
	def led(self, n, r, g, b):
		self.i2c.writeto(self.ADDR, bytes([self.CMD_LED, n&0xFF, r&0xFF, g&0xFF, b&0xFF]))
	
	def buzzer(self, freq, duration=0):
		freq_hi = (freq >> 8)&0xFF
		freq_lo = freq&0xFF
		duration_hi = (duration >> 8)&0xFF
		duration_lo = duration&0xFF
		self.i2c.writeto(self.ADDR, bytes([self.CMD_BUZZER, freq_hi, freq_lo, duration_hi, duration_lo]))
		
	def off(self):
		self.i2c.writeto(self.ADDR, bytes([self.CMD_OFF]))
		
	def read_raw(self):
		return self.i2c.readfrom(self.ADDR, 2)
		
	def read_usb(self):
		return (self.read_raw()[0]>>6)&0x01
		
	def read_buttons(self):
		return (self.read_raw()[0])&0x3F
	
	def buttonPressed(self, btn):
		return (self.read_buttons() >> btn)&0x01
	
	def read_battery(self):
		self.read_raw()[1]

i2c = I2C(scl=Pin(22), sda=Pin(23))

lcd = ERC12864.ERC12864(i2c)
dev = Samd(i2c)


#Framebuffer
_fb_buf = bytearray([0]*1024)
fb = framebuf.FrameBuffer(_fb_buf, 128, 64, framebuf.MONO_VLSB)

def fb_write():
	global fb_buf
	lcd.writeFlipped(_fb_buf)
