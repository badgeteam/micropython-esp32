import helpers.scheduler as scheduler

def new(target, callback, hfpm=False):
	return scheduler.new(target, callback, hfpm)
    
def idle_time():
	return scheduler.idle_time()   
    
def delete(callback):
	return scheduler.delete(callback)

def update(target, callback):
	return scheduler.update(target, callback)

def activate(p):
	return scheduler.start(p)
    
def stop():
	return scheduler.stop()
