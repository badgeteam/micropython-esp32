import network, badge, gc, version

sta_if = False

def init():
    global sta_if
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    ssid = badge.nvs_get_str('badge', 'wifi.ssid', version.wifi_ssid)
    password = badge.nvs_get_str('badge', 'wifi.password', version.wifi_password)
    if password:
        sta_if.connect(ssid, password)
    else:
        sta_if.connect(ssid)

gc.collect()
