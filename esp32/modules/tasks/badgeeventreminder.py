# File: badgeeventreminder.py
# Version: 1
# Description: Easter egg
# License: MIT
# Authors: Renze Nicolai <renze@rnplus.nl>

import virtualtimers, time, appglue, badge

# Tue Aug  8 13:30:00 2017 (CEST)
# (warn 10 minutes before the event)
whenToTrigger = 1502191800 - 600

def ber_task():
    global whenToTrigger
    # braindead time.time() implementation. it's 2 hours in the
    # future.
    now = time.time() - 7200
    if now >= whenToTrigger and now < whenToTrigger + 600 + 3600:
        badge.nvs_set_u8('badge','evrt',1)
        print("BADGE EVENT REMINDER ACTIVATED")
        appglue.start_app("badge_event_reminder")
    idleFor = whenToTrigger - now
    if idleFor < 0:
        idleFor = 0
    return idleFor * 1000

def enable():
    if badge.nvs_get_u8('badge','evrt',0)==0:
        virtualtimers.new(1, ber_task)

def disable():
    virtualtimers.delete(ber_task)
