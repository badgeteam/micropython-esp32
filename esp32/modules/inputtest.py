import ugfx

def up(p):
	print("up",p)
def down(p):
	print("down",p)
def left(p):
	print("left",p)
def right(p):
	print("right",p)
def b(p):
	print("b",p)
def start(p):
	print("start",p)

ugfx.input_init()
ugfx.input_attach(ugfx.JOY_UP, up)
ugfx.input_attach(ugfx.JOY_DOWN, down)
ugfx.input_attach(ugfx.JOY_LEFT, left)
ugfx.input_attach(ugfx.JOY_RIGHT, right)
ugfx.input_attach(ugfx.BTN_B, b)
ugfx.input_attach(ugfx.BTN_START, start)

print("Press a button!")
