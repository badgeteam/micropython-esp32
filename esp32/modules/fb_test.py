import framebuf, font_writer, font_roboto_12, badge, disobey

#Allocate a buffer
buf = bytearray([0]*4736)

#Create a framebuffer object using the buffer
fb = framebuf.FrameBuffer(buf, 296, 128, framebuf.MONO_HMSB)

#Draw some stuff
fb.line(0,0,128,128,1)
fb.fill_rect(128,64,32,32,1)
fb.text("Hello, world!", 32, 15, 1)

#Draw text using a font
fontWriter = font_writer.Writer(fb, font_roboto_12, 296, 128, True)
fontWriter.set_textpos(32, 32)
fontWriter.printstring("Roboto 12 test")

#Invert the buffer
for i, v in enumerate(buf):
	buf[i] = 0xFF & ~ v

#Send to the e-ink display
badge.eink_display_raw(bytes(buf), 0)
