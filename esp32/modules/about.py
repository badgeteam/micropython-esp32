import ugfx, appglue, term, sys,time, version

names = ["Niek Blankers", "Sebastian Oort", "Bas van Sisseren", "Jeroen Domburg", "Christel Sanders", "Markus Bechtold", "Thomas Roos", "Anne Jan Brouwer", "Renze Nicolai", "Aram Verstegen", "Arnout Engelen", "Alexandre Dulaunoy", " Eric Poulsen", "Damien P. George", "uGFX", "EMF Badge Team"]

def action_exit(pushed):
    if (pushed):
        appglue.home()

def draw_name(x,y,name):
    ugfx.string(x, y, name, version.font_default, ugfx.BLACK)
    ugfx.flush()

def show_names():
	global names
	c = False
	y = 10
	nos = 0
	ugfx.clear()
	
	term.header(True, "About")
	print("Developers:")
	for n in range(0, len(names)):
		print(" - "+names[n])
	
	for n in range(0, len(names)):
		draw_name(5,y,names[n])
		y += 15
		nos += 1
		if (nos > 3):
			nos = 0
			y = 10
			time.sleep(1)
			ugfx.clear()

def main():
    ugfx.input_init()
    ugfx.input_attach(ugfx.BTN_B, action_exit)
    ugfx.input_attach(ugfx.BTN_START, action_exit)
    show_names()
    sys.stdin.read(1) #Wait for any key
    action_exit(True)
    

main()
