import sys

from slotobahn import app

try:
    app.run(debug=True)
except KeyboardInterrupt:
    print 'Server stopped by the user'
    sys.exit(0)
