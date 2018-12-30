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
		write(bytes([0]*1024))
		
	def flip(self, buf):
		new = bytearray([0]*1024)
		for i in range(1024):
			a = buf[i]
			new[1023-i] = ((a&1)<<7)+(((a>>1)&1)<<6)+(((a>>2)&1)<<5)+(((a>>3)&1)<<4)+(((a>>4)&1)<<3)+(((a>>5)&1)<<2)+(((a>>6)&1)<<1)+((a>>7)&1)
		return new
			
	def writeFlipped(self, buf):
		self.write(self.flip(buf))
			
	def _initdisplay(self):
		self.i2c.writeto(0x38,bytes([0x2f,0xA2,0xA1,0xC8,0x24,0x81,37,0x40,0xAF]));

