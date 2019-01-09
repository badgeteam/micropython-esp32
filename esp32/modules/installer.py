import ugfx, badge, network, gc, time, urequests, appglue, sys, appglue, easydraw, version

def connectWiFi():
    nw = network.WLAN(network.STA_IF)
    if not nw.isconnected():
        nw.active(True)
        ssid = badge.nvs_get_str('badge', 'wifi.ssid', version.wifi_ssid)
        password = badge.nvs_get_str('badge', 'wifi.password', version.wifi_password)
        nw.connect(ssid, password) if password else nw.connect(ssid)

        appglue.msg("Connecting to '"+ssid+"'...")

        timeout = 150
        while not nw.isconnected():
            time.sleep(0.1)
            timeout = timeout - 1
            if (timeout<1):
                appglue.msg("Timeout while connecting!")
                nw.active(True)
                return False
    return True

def show_description(active):
	if active:
		#packages[options.selected_index()]["description"]
		ugfx.flush()

def select_category(active):
	if active:
		global categories
		global options
		index = options.selected_index()
		if categories[index]["eggs"] > 0:
			category = categories[index]["slug"]
			list_apps(category)

def list_apps(slug):
	global options
	global packages

	ugfx.input_attach(ugfx.JOY_UP, 0)
	ugfx.input_attach(ugfx.JOY_DOWN, 0)
	ugfx.input_attach(ugfx.BTN_B, 0)
	ugfx.input_attach(ugfx.BTN_START, 0)

	while options.count() > 0:
		options.remove_item(0)
	easydraw.msg("Downloading list of eggs...")
	ugfx.flush(ugfx.LUT_FULL)

	try:
		f = urequests.get("https://badge.disobey.fi/eggs/category/%s/json" % slug, timeout=30)
		try:
			packages = f.json()
		finally:
			f.close()
	except BaseException as e:
		print("[Installer] Failed to download list of eggs:")
		sys.print_exception(e)
		easydraw.msg("Failed :(")
		ugfx.flush(ugfx.LUT_FULL)
		list_categories()
		gc.collect()
		return

	for package in packages:
		options.add_item("%s rev. %s" % (package["name"], package["revision"]))
	options.selected_index(0)

	ugfx.input_attach(ugfx.JOY_UP, show_description)
	ugfx.input_attach(ugfx.JOY_DOWN, show_description)
	ugfx.input_attach(ugfx.BTN_A, install_app)
	ugfx.input_attach(ugfx.BTN_B, lambda pushed: list_categories() if pushed else False)
	ugfx.input_attach(ugfx.BTN_START, lambda pushed: appglue.start_app('') if pushed else False)

	show_description(True)
	gc.collect()

def start_categories(pushed):
	if pushed:
		list_categories()

def start_app(pushed):
	if pushed:
		global selected_app
		appglue.start_app(selected_app)

def install_app(active):
	if active:
		global options
		global packages
		global selected_app

		index = options.selected_index()

		ugfx.input_attach(ugfx.JOY_UP, 0)
		ugfx.input_attach(ugfx.JOY_DOWN, 0)
		ugfx.input_attach(ugfx.BTN_A, 0)
		ugfx.input_attach(ugfx.BTN_B, 0)
		ugfx.input_attach(ugfx.BTN_START, 0)

		easydraw.msg(packages[index]["name"], "Installing...", True)

		latest = False
		import woezel
		selected_app =  packages[index]["slug"]
		try:
			woezel.install(selected_app)
		except woezel.LatestInstalledError:
			latest = True
		except:
			easydraw.msg("Failed :(")
			time.sleep(4)
			list_categories()
			return

		ugfx.clear(ugfx.WHITE)
		if latest:
			easydraw.msg("Already installed:", "Done :)", True)
		else:
			easydraw.msg("Installed:", "Done :)", True)
		easydraw.msg(packages[index])

		ugfx.input_attach(ugfx.BTN_START, start_app)
		ugfx.input_attach(ugfx.BTN_B, start_categories)

		ugfx.flush()
		gc.collect()

def list_categories():
	global options
	global categories

	try:
		categories
	except:
		ugfx.input_init()
		appglue.msg('Getting categories')
		try:
			f = urequests.get("https://badge.disobey.fi/eggs/categories/json", timeout=30)
			categories = f.json()
		except:
			appglue.msg('Failed :(')
			appglue.start_app('launcher', False)

			f.close()
		appglue.msg('Done!')
		options = ugfx.List(0,0,int(ugfx.width()),ugfx.height())



	ugfx.input_attach(ugfx.JOY_UP, lambda pushed: ugfx.flush() if pushed else False)
	ugfx.input_attach(ugfx.JOY_DOWN, lambda pushed: ugfx.flush() if pushed else False)
	ugfx.input_attach(ugfx.BTN_START, select_category)
	ugfx.input_attach(ugfx.BTN_B, lambda pushed: appglue.start_app("launcher", False) if pushed else False)

	ugfx.clear(ugfx.WHITE)
	ugfx.flush()

	while options.count() > 0:
		options.remove_item(0)
	for category in categories:
		options.add_item("%s (%d) >" % (category["name"], category["eggs"]))
	options.selected_index(0)
	ugfx.flush(ugfx.LUT_FULL)
	gc.collect()


if not connectWiFi():
	appglue.msg('WiFi failed :(')
	appglue.start_app('launcher', False)
else:
	list_categories()
