from raspiomix import Raspiomix
from bottle import route, run
from adxl345 import ADXL345
import time
import json
  
adxl345 = ADXL345()
r = Raspiomix()

@route('/accelero')

def accelero():
    axes = adxl345.getAxes(True)
    return json.dumps([{'x' : axes['x'], 'y' : axes['y'], 'z' : axes['z']}])

@route('/temp')

def temp():
    return json.dumps([{'temperature' : r.readAdc(0)*10 }])

run(host='0.0.0.0', port=8080, debug=True)
"""
while True:    
    axes = adxl345.getAxes(True)
    print "   x = %.3fG" % ( axes['x'] )
    print "   y = %.3fG" % ( axes['y'] )
    print "   z = %.3fG" % ( axes['z'] )
    print " "
    time.sleep(0.1)
"""