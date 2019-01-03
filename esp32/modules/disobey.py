import framebuf
import badge

#Framebuffer
_fb_buf = bytearray([0]*1024)
fb = framebuf.FrameBuffer(_fb_buf, 128, 64, framebuf.MONO_VLSB)

def write():
	global fb_buf
	badge.lcdWrite(_fb_buf)
