import machine, sys

tasks = []
timer = machine.Timer(0)
period = 0
debugEnabled = False

def start(p=50):
	"""
	Start the scheduler
	Argument: resolution/period in milliseconds
	"""
	global timer, period
	if p<1:
		return period
	if period==0:
		period = p
		timer.init(period=p, mode=machine.Timer.PERIODIC, callback=_timer_callback)
	return period

def stop():
	"""
	Stop the scheduler
	"""
	global timer, period
	timer.deinit()
	period = 0

def new(target, callback, hfpm=False):
	"""
	Create a new task.
	Arguments: time until callback is called, callback, hide from power management
	Note: updates the existing task instead if the callback has already been registered
	"""
	global tasks, period
	if target < period:
		target = period
	if not update(target, callback):
		global tasks
		item = {"pos":0, "target":target, "cb":callback, "hfpm":hfpm}
		tasks.append(item)
	return callback

def update(target, callback):
	"""
	Update an existing task
	"""
	global tasks, period
	if target < period:
		target = period
	found = False
	for i in range(0, len(tasks)):
		if (tasks[i]["cb"]==callback):
			tasks[i]["pos"] = 0
			tasks[i]["target"] = target
			found = True
	return found

def delete(callback):
	"""
	Delete an existing task
	"""
	global tasks
	found = False
	for i in range(0, len(tasks)):
		if (tasks[i]["cb"]==callback):
			found = True
			break
	
	tasks = list(task for task in tasks if task['cb']!=callback)
	
	return found

def printTasks():
	"""
	Prints the internal state of the scheduler
	"""
	global tasks, period
	if period > 0:
		print("Scheduler active with period "+str(period)+"ms")
	else:
		print("Scheduler disabled")
	print("")
	print("Task\tTarget\tPosition\tRemaining\tHidden")
	print("====\t======\t========\t=========\t======")
	for i in range(0, len(tasks)):
		print(tasks[i]["cb"],"\t",tasks[i]["target"],"\t",tasks[i]["pos"],"\t",tasks[i]['target']-tasks[i]['pos'],"\t",tasks[i]['hfpm'])
	print("")

def idle_time():
    """
    Returns time until next task in ms, ignores tasks hidden from power management
    """
    global tasks
    idleTime = 86400000 # One day (causes the badge to sleep forever)
    for i in range(0, len(tasks)):
        timeUntilTaskExecution = tasks[i]['target']-tasks[i]['pos']
        if not tasks[i]["hfpm"]:
            if timeUntilTaskExecution<0:
                timeUntilTaskExecution = 0
            if timeUntilTaskExecution<idleTime:
                idleTime = timeUntilTaskExecution
    return idleTime
            
def _timer_callback(tmr):
	"""
	Internal function! Callback for the timer
	"""
	global tasks
	global period
	s = len(tasks)
	cleanup = False
	for i in range(0, len(tasks)):
		tasks[i]["pos"] += period
		if tasks[i]["pos"] > tasks[i]["target"]:
			try:
				newTarget = tasks[i]["cb"]()
			except BaseException as e:
				print("[SCHEDULER] An error occured in task",task[i],". The task has been terminated.")
				sys.print_exception(e)
				newTarget = -1
			if not newTarget == None:
				if newTarget > 0:
					tasks[i]["pos"] = 0
					tasks[i]["target"] = newTarget
				else:
					tasks[i]["pos"] = -1
					tasks[i]["target"] = -1
					cleanup = True
	if cleanup:
		tasks = list(task for task in tasks if task["pos"]>=0)
