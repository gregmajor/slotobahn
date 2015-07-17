import sys
import RPi.GPIO as GPIO

from slotobahn import app

try:
    print 'Starting server...'
    app.run(host='0.0.0.0', port=80, debug=True)
except KeyboardInterrupt:
    print 'Server stopped by the user'
    GPIO.cleanup()
    sys.exit(0)
