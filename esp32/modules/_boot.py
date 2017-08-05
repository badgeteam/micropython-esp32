import badge, gc, uos

try:
    badge.mount_root()
    uos.mount(uos.VfsNative(None), '/')
    with open("/boot.py", "r") as f:
        f.close()

except OSError:
    import inisetup
    vfs = inisetup.setup()

gc.collect()
