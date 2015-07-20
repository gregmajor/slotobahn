import json
import logging
import socket
import dateutil.parser as date_parser
from datetime import datetime

from motor import Motor
from blinker import Blinker
from display import Display
from database import Database
from consumer import Consumer


class Clock(object):
    """This is the clock aggregate root.
    """

    def __init__(self, configuration):
        """Create a new instance of the clock class.
        """
        self._configuration = configuration
        self._logger = logging.getLogger(__name__)

        self._motor = Motor(self._configuration)
        self._blinker = Blinker(self._configuration)
        self._display = Display(self._configuration)
        self._database = Database(self._configuration)
        self._consumer = Consumer(self._configuration, self.on_message)

    @property
    def blinker(self):
        """The blinker.
        """
        return self._blinker

    @property
    def consumer(self):
        """The RabbitMQ consumer.
        """
        return self._consumer

    @property
    def database(self):
        """The database.
        """
        return self._database

    @property
    def display(self):
        """The display.
        """
        return self._display

    @property
    def ip_address(self):
        """The IP address.
        """
        return socket.gethostbyname(socket.gethostname())

    @property
    def motor(self):
        """The clock motor.
        """
        return self._motor

    def on_message(self, unused_channel, basic_deliver, properties, body):
        """Invoked when a message is delivered from RabbitMQ. The channel is passed for your convenience. The
        basic_deliver object that is passed in carries the exchange, routing key, delivery tag and a redelivered flag
        for the message. The properties passed in is an instance of BasicProperties with the message properties and the
        body is the message that was sent.

        :param pika.channel.Channel unused_channel: The channel object
        :param pika.Spec.Basic.Deliver: basic_deliver method
        :param pika.Spec.BasicProperties: properties
        :param str|unicode body: The message body
        """
        self._logger.info('Received message # %s from %s: %s', basic_deliver.delivery_tag, properties.app_id, body)

        self._motor.turn(15, 50)
        
        #self._blinker.blink()

        order_year = datetime.today().year
        order_month = datetime.today().month

        #if body is not None:
        #    payload = json.loads(body)

        #    if payload['Order'] is not None:
        #        order = payload['Order']

        #        if order is not None:

        #            order_date = date_parser.parse(order['OrderDate'])

        #            self._logger.info('Order date is %s', order_date.strftime("%Y-%m-%d %H:%M:%S"))

        #            order_year = int(order_date.year)

        #            self._logger.info('Order year is %i', order_year)

        #            order_month = int(order_date.month)

        #            self._logger.info('Order month is %i', order_month)

        self._logger.info('Current order count is %i', self._database.order_count)

        self._database.record_order(order_year, order_month)

        self._display.write("%i orders" % self._database.order_count)
