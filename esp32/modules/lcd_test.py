import framebuf, font_writer, font_roboto_12, badge, disobey

#Allocate a buffer
buf = bytearray([0]*1024)

#Create a framebuffer object using the buffer
fb = framebuf.FrameBuffer(buf, 128, 64, framebuf.MONO_VLSB)

#Draw some stuff
fb.line(0,0,128,64,1)
fb.text("Hello, world!", 0, 0, 1)

#Draw text using a font
#fontWriter = font_writer.Writer(fb, font_roboto_12, 0, 40, True)
#fontWriter.set_textpos(0, 32)
#fontWriter.printstring("Roboto 12 test")

#Send to the LCD
disobey.dev.backlight(255)
disobey.lcd.write(buf)
