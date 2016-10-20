import time
import os
a = "home/pi/raspiomix/mixtrem.py"

while True:
	time.sleep(6)
	os.execlp('python', 'mixtrem.py')
