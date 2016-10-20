from raspiomix import Raspiomix
import time

r = Raspiomix()

while True:
	if r.readAdc(3) > 0.03378:
	   print "%f Volt !" % r.readAdc(3)