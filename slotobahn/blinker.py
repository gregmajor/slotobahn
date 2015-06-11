import time
import logging

try:
    import RPi.GPIO as GPIO
except ImportError:
    print("Could not import GPIO")


class Blinker(object):
    """This is a class that represents the blinker.
    """

    def __init__(self, configuration):
        """Create a new instance of the blinker class.
        """
        self._configuration = configuration
        self._logger = logging.getLogger(__name__)

        self._pin = self._configuration.blinker_pin

        # Use BCM GPIO references rather than physical pin numbers
        if self._configuration.simulate is False:
            GPIO.setmode(GPIO.BCM)

        # Set the output pin as output and reset to low
        self._logger.info("Setting up GPIO pin %i" % self._pin)
        if self._configuration.simulate is False:
            GPIO.setup(self._pin, GPIO.OUT)
            GPIO.output(self._pin, False)

    @property
    def pin(self):
        """Defines the GPIO pin to use.
        """
        return self._pin

    @pin.setter
    def pin(self, value):
        self._pin = value

    def blink(self, count=3, speed=0.25):
        """Blinks the blinker.

          :param int count: The number of times to blink.
          :param float speed: How fast to blink (in seconds).
        """
        for i in range(0, count):
            self._logger.info("Blinking %i times" % count)

            # Switch on
            if self._configuration.simulate is False:
                GPIO.output(self._pin, True)

            time.sleep(speed)

            # Switch off
            if self._configuration.simulate is False:
                GPIO.output(self._pin, False)

            time.sleep(speed)
