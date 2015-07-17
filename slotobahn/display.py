import logging

try:
    import Adafruit_CharLCD as Lcd
except ImportError:
    print("Could not import Adafruit CharLCD")


class Display(object):
    """This is a class that represents the LCD screen.
    """

    def __init__(self, configuration):
        """Create a new instance of the LCD class.
        """
        self._configuration = configuration
        self._logger = logging.getLogger(__name__)

        self._static_message = self._configuration.static_message

        if self._configuration.simulate is False:
            self._lcd = Lcd.Adafruit_CharLCDPlate(busnum=1)

        self.write_static_message()

    @property
    def static_message(self):
        """Defines a static message to display on the first row.
        """
        return self._static_message

    def clear(self):
        """Clears the bottom row of the display.
        """
        self._logger.info("Clearing the display")

        if self._configuration.simulate is False:
            self._lcd.set_cursor(2, 1)
            self._lcd.message('' * 16)

    def write(self, message):
        """Writes a message to the display.
        :param message: The message to write.
        """
        self._logger.info("Writing message: %s" % message)

        if self._configuration.simulate is False:
            self.clear()
            self.set_cursor(2, 1)
            self._lcd.message(message.center(16, ''))

    def write_static_message(self):
        """Writes the static message to the display.
        """
        self._logger.info("Writing static message: %s" % self._static_message)

        if self._configuration.simulate is False:
            self._lcd.clear()
            centered_message = self._static_message.center(16, ' ')
            self._lcd.message(centered_message)
