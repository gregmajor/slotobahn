import sys
import RPi.GPIO as GPIO

from slotobahn import app

try:
    app.run(debug=True)
except KeyboardInterrupt:
    print 'Server stopped by the user'
    GPIO.cleanup()
    sys.exit(0)
