from machine import Pin, PWM
from time import sleep_ms

optics_sleep = 50

pin_rx_enable = Pin(21, Pin.OUT)
pin_rx        = Pin(18, Pin.IN)
pin_tx        = Pin(19, Pin.OUT)
pwm_tx        = PWM(pin_tx, freq=38000, duty=0)

def rawTx(p):
	pwm_tx.duty(512*p)
	
def rawRx():
	return not pin_rx.value()

def txByte(byte):
	for bit in range(8):
		rawTx((byte>>(7-bit))&1)
		sleep_ms(optics_sleep)

def tx(data):
	rawTx(False)
	sleep_ms(optics_sleep*8)
	txByte(0b11101010)
	txByte(0b10101011)
	for char in data:
		txByte(ord(char))
	rawTx(False)

buf = 0

def _rxBit():
	global buf
	buf = ((buf<<1) + rawRx()*1)&0xFFFF
	sleep_ms(optics_sleep)

def _rxByte():
	global buf
	for i in range(8):
		_rxBit()
	return buf & 0xFF

def _rxWait(timeout=100):
	global buf
	cnt = 0
	while True:
		_rxBit()
		if buf&0xFFFF == 0b1110101010101011:
			buf = 0
			return True
		#rxDebug()
		cnt+=1
		if cnt > timeout:
			return False

def rx(timeout=100):
	pin_rx_enable.value(True)
	global buf
	string = ""
	buf = 0
	if not _rxWait(timeout):
		pin_rx_enable.value(False)
		return None
	while True:
		b = _rxByte()
		if b < 1:
			pin_rx_enable.value(False)
			return string
		string += chr(b)
		

# BACKGROUND IR RECV

# !!! DOES NOT WORK YET !!!

def rxBgDebug(cnt=16, n="\n"):
	global bgBuf
	for i in range(cnt):
		a = (bgBuf>>(cnt-i-1))&1
		print(a,end="")
	print(n,end="")

def initBg(callback):
	global _irCb, bgBuf, bgState
	bgBuf = 0
	bgState = 0
	_irCb = callback
	vt.delete(irTask)
	vt.new(1, irTask, True)

def irTask():
	global bgState, bgBuf, bgByteCnt
	bgBuf = ((bgBuf<<1) + rawRx()*1)&0xFFFF
	if bgState == 0:
		bgBytecnt = 0
		if bgBuf&0xFFFF == 0b1110101010101011:
			bgState = 1
			print("P MATCH")
		rxBgDebug()
	elif bgState == 1:
		rxDebug(8)
		if bgByteCnt>=7:
			bgByteCnt = 0
			print("RX",chr(bgBuf&0xFF),bin(bgBuf&0xFF))
		else:
			bgByteCnt += 1
	return optics_sleep
