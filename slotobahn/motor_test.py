from motor import Motor
from configuration import Configuration
import logging

LOG_FORMAT = '%(levelname) -10s %(asctime)s %(name) -30s %(funcName) -35s %(lineno) -5d: %(message)s'
LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

log_file_handler = logging.FileHandler('slotobahn.log')
app.logger.addHandler(log_file_handler)

configuration = Configuration()

motor = Motor(configuration)

motor.turn(20, 50)
