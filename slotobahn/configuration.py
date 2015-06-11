import ConfigParser
import logging


class Configuration(object):
    """This class represents the application configuration.
    """

    def __init__(self):
        self._parser = ConfigParser.ConfigParser()
        self._logger = logging.getLogger(__name__)

        self._parser.read("configuration.ini")

    @property
    def admin_user(self):
        return self._parser.get('General', 'AdminUser')

    @property
    def admin_password(self):
        return self._parser.get('General', 'AdminPassword')

    @property
    def blinker_pin(self):
        return self._parser.getint('Blinker', 'BlinkerPin')

    @property
    def database_file_name(self):
        return self._parser.get('Database', 'DatabaseFileName')

    @property
    def exchange(self):
        return self._parser.get('Consumer', 'Exchange')

    @property
    def exchange_type(self):
        return self._parser.get('Consumer', 'ExchangeType')

    @property
    def name(self):
        return self._parser.get('General', 'Name')

    @property
    def queue(self):
        return self._parser.get('Consumer', 'Queue')

    @property
    def routing_key(self):
        return self._parser.get('Consumer', 'RoutingKey')

    @property
    def schema_file_name(self):
        return self._parser.get('Database', 'SchemaFileName')

    @property
    def static_message(self):
        return self._parser.get('Display', 'StaticMessage')

    @property
    def step_direction(self):
        return self._parser.getint('Motor', 'StepDirection')

    @property
    def url(self):
        return self._parser.get('Consumer', 'Url')
