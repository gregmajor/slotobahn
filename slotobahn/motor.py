import time
import logging

try:
    import RPi.GPIO as GPIO
except ImportError:
    print("Could not import GPIO")


class Motor(object):
    """This is a class that represents the bi-polar stepper motor.
    """

    def __init__(self, configuration):
        """Create a new instance of the motor class.
        """
        self._configuration = configuration
        self._logger = logging.getLogger(__name__)
        self._sequence = None
        self._step_direction = self._configuration.step_direction
        self._step_pins = None
        
        # Use BCM GPIO references rather than physical pin numbers
        if self._configuration.simulate is False:
            GPIO.setmode(GPIO.BCM)

        # Set all pins as output and reset to low
        for pin in self.step_pins:
            self._logger.info("Setting up GPIO pin %i" % pin)

            if self._configuration.simulate is False:
                GPIO.setup(pin, GPIO.OUT)
                GPIO.output(pin, False)

    @property
    def sequence(self):
        """Define the motor self.sequence as shown in manufacturers datasheet.
        """
        if self._sequence is None:
            self._sequence = [[1, 0, 0, 0],
                              [1, 1, 0, 0],
                              [0, 1, 0, 0],
                              [0, 1, 1, 0],
                              [0, 0, 1, 0],
                              [0, 0, 1, 1],
                              [0, 0, 0, 1],
                              [1, 0, 0, 1]]
        return self._sequence

    @sequence.setter
    def sequence(self, value):
        self._sequence = value

    @property
    def step_direction(self):
        """Determines which direction the motor turns. Set to 1 or 2 for clockwise. Set to -1 or -2 for
        counter-clockwise.
        """
        if self._step_direction is None:
            self._step_direction = 2

        return self._step_direction

    @step_direction.setter
    def step_direction(self, value):
        self._step_direction = value

    @property
    def step_pins(self):
        """Defines the GPIO pins to use. Physical pins 11, 15, 16, 18.
        """
        if self._step_pins is None:
            self._step_pins = [17, 22, 23, 24]

        return self._step_pins

    @step_pins.setter
    def step_pins(self, value):
        self._step_pins = value

    def turn(self, wait_time=20, duration=20):
        """Turns the motor.

          :param int wait_time: How long to wait between steps.
          :param int duration: How long to turn.
        """
        # Determine how many steps we must take based on the element count in the self.sequence
        step_count = len(self.sequence) - 1

        wait_time_in_ms = int(wait_time) / float(1000)

        elapsed = 0
        step_counter = 0

        while elapsed < duration:

            for pin in range(0, 4):

                # Get the pin
                current_pin = self.step_pins[pin]

                self._logger.info(step_counter)
                self._logger.info(pin)

                # Go high or low on the pin depending on the element value
                if self.sequence[step_counter][pin] != 0:
                    self._logger.info("Step %i - Setting pin %i HIGH" % (step_counter, current_pin))

                    #if self._configuration.simulate is False:
                    GPIO.output(current_pin, True)
                else:
                    self._logger.info("Step %i - Setting pin %i LOW" % (step_counter, current_pin))

                    #if self._configuration.simulate is False:
                    GPIO.output(current_pin, False)

                step_counter += self.step_direction

                elapsed += 1

                # If we reach the end of the self.sequence start again
                if step_counter >= step_count:
                    step_counter = 0
                if step_counter < 0:
                    step_counter = step_count

                # Wait before moving on to avoid over-driving the controller
                self._logger.info("Waiting for %i" % wait_time_in_ms)

                time.sleep(wait_time_in_ms)
