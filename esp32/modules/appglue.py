import ugfx, esp, badge, deepsleep, appglue

def start_app(app, display = True):
    if display:
        easydraw.msg(app, "Loading...", True)
    esp.rtcmem_write_string(app)
    deepsleep.reboot()

def home():
    start_app("")

def start_ota():
    esp.rtcmem_write(0,1)
    esp.rtcmem_write(1,254)
    deepsleep.reboot()

#def start_bpp(duration):
#    print("[BPP] Duration = "+str(duration))
#    esp.rtcmem_write(0,2)
#    esp.rtcmem_write(1,253)
#    deepsleep.reboot()
