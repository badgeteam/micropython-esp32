#ERC12864 i2c display driver

class ERC12864:
	def __init__(self, i2c):
		self.i2c=i2c
		self._initdisplay()
			
	def _set_page_address(self,p):
		self.i2c.writeto(0x38,bytes([(0xb0|p)]))
	
	def _set_column(self,c):
		self.i2c.writeto(0x38,bytes([(0x10|(c>>4)),((0x0f&c)|0x04)]))
	
	def write(self,buf):
		for page in range(8):
			self._set_page_address(page)
			for num in range(4):
				self._set_column(num*0x20)
				start = 128*page+32*num
				self.i2c.writeto(0x39,bytes(buf[start:start+32]))
	
	def clear(self):
		for i in range(8):
			self._set_page_address(i)
			for num in range(4):
				self._set_column(num*0x20)
				self.i2c.writeto(0x39,bytes([0]*0x20))
			
	def _initdisplay(self):
		self.i2c.writeto(0x38,bytes([0x2f,0xA2,0xA1,0xC8,0x24,0x81,37,0x40,0xAF]));
