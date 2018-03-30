from pykeyboard import PyKeyboard
import time

k = PyKeyboard()

def createTerminal():
    k.press_keys([k.control_key,k.alt_key,'t'])

def writeTerminal():
    k.tap_key('-', n = 5, interval = 0.7)
    k.press_keys([k.shift_key,'<'])
    k.type_string(' by Alan')
    time.sleep(1.2)
    k.tap_key(k.backspace_key, n = 14, interval = 0.3)

def exitTerminal():
    k.type_string('exit')
    time.sleep(0.5)
    k.tap_key(k.enter_key)

createTerminal()
time.sleep(0.7)
writeTerminal()
time.sleep(0.7)
exitTerminal()
