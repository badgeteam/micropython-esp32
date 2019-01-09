import easywifi, easydraw, badge, time, version

def download_info():
    import urequests as requests
    easydraw.msg("Checking OTA...")
    result = False
    try:
        data = requests.get("https://badge.disobey.fi/firmware/version")
    except:
        easydraw.msg("Error 1 :(")
        time.sleep(5)
        return False
    try:
        result = data.json()
    except:
        data.close()
        easydraw.msg("Error 2 :(")
        time.sleep(5)
        return False
    data.close()
    return result

def available(update=False):
    if update:
        if not easywifi.status():
            if not easywifi.enable():
                return badge.nvs_get_u8('badge','OTA.ready',0)

        info = download_info()
        if info:
            if info["build"] > version.build:
                badge.nvs_set_u8('badge','OTA.ready',1)
                return True

        badge.nvs_set_u8('badge','OTA.ready',0)
    return badge.nvs_get_u8('badge','OTA.ready',0)
