from slotobahn import app

import datetime
from functools import wraps
import logging

from flask import Flask, render_template, request, jsonify
from flask.ext.assets import Bundle, Environment

from clock import Clock
from configuration import Configuration

configuration = Configuration()

LOG_FORMAT = '%(levelname) -10s %(asctime)s %(name) -30s %(funcName) -35s %(lineno) -5d: %(message)s'
LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

log_file_handler = logging.FileHandler('slotobahn.log')
app.logger.addHandler(log_file_handler)

bundles = {
    'main_js': Bundle(
        'js/lib/jquery-2.1.4.min.js',
        'js/lib/bootstrap.min.js',
        'js/lib/Chart.min.js',
        'js/clock.js',
        output='gen/main.js'),
    'main_css': Bundle(
        'css/bootstrap.min.css',
        'css/bootstrap-theme.min.css',
        'css/main.css',
        output='gen/main.css')
}

assets = Environment(app)
assets.register(bundles)

clock = Clock(configuration)

def authenticate(username, password):
    """Checks authentication.
    """
    return username == configuration.admin_user and password == configuration.admin_password

def send_authentication_response():
    """Shows the authentication response.
    """
    message = {'message': "Authenticate."}
    response = jsonify(message)

    response.status_code = 401
    response.headers['WWW-Authenticate'] = 'Basic realm="Example"'

    return response

def requires_authentication(f):
    """A decorator that requires authentication.

    :param f: The function being decorated.
    :return: The decoration.
    """

    @wraps(f)
    def decorated(*args, **kwargs):

        authorization = request.authorization

        if not authorization:
            return send_authentication_response()

        elif not authenticate(authorization.username, authorization.password):
            return send_authentication_response()

        return f(*args, **kwargs)

    return decorated

@app.errorhandler(403)
def forbidden(e):
    template_data = {
        'name': configuration.name
    }
    return render_template('403.html', **template_data), 403

@app.errorhandler(404)
def page_not_found(e):
    template_data = {
        'name': configuration.name
    }
    return render_template('404.html', **template_data), 404

@app.errorhandler(404)
def internal_error(e):
    template_data = {
        'name': configuration.name
    }
    return render_template('500.html', **template_data), 500

@app.route("/")
def index():
    """The main page.
    """
    template_data = {
        'name': configuration.name,
        'order_total': "%i total orders!" % clock.database.order_count
    }

    return render_template('dashboard.html', **template_data)

@app.route("/about")
def about():
    """The about page.
    """
    template_data = {
        'name': configuration.name
    }

    return render_template('about.html', **template_data)

@app.route("/admin")
@requires_authentication
def admin():
    """The admin page.
    """
    now = datetime.datetime.now()
    time_string = now.strftime("%Y-%m-%d %H:%M")
    ip_address = clock.ip_address
    template_data = {
        'name': configuration.name,
        'time': time_string,
        'simulate': configuration.simulate,
        'ip_address': ip_address,
        'step_direction': clock.motor.step_direction,
        'step_pins': clock.motor.step_pins,
        'sequence': clock.motor.sequence,
        'exchange': clock.consumer.exchange,
        'exchange_type': clock.consumer.exchange_type,
        'queue': clock.consumer.queue,
        'routing_key': clock.consumer.routing_key,
        'url': clock.consumer.url,
        'blinker_pin': clock.blinker.pin,
        'database_file_name': configuration.database_file_name,
        'schema_file_name': configuration.schema_file_name,
        'static_message': configuration.static_message
    }

    return render_template('admin.html', **template_data)

@app.route("/blinker/blink")
def blinker_blink():
    """Blinks the blinker, man.
    """
    count = 1
    speed = 1
    LOGGER.info("Blinking the blinker %i times with a speed of %i" % (count, speed))
    clock.blinker.blink(count, speed)
    return jsonify(result='Blinker Blinked!')

@app.route("/consumer/start")
def consumer_start():
    """Starts the consumer.
    """
    LOGGER.info('Starting the consumer')
    clock.consumer.start()
    return jsonify(result='Consumer Started!')

@app.route("/consumer/stop")
def consumer_stop():
    """Stops the consumer.
    """
    LOGGER.info('Stopping the consumer')
    clock.consumer.stop()
    return jsonify(result='Consumer Stopped!')

@app.route("/orders")
def orders():
    """Gets all orders.
    """
    orders = clock.database.orders

    return jsonify(orders=orders)

@app.route("/orders/chartdata")
def orders_chartdata():
    """Gets the chart data.
    """
    chart_data = clock.database.chart_data

    return jsonify(chart_data)

@app.route("/orders/<int:year>")
def orders_ordersforyear(year):
    """Gets the orders for a particular year.
    """
    orders = clock.database.get_orders_for_year(year)

    return jsonify(orders_for_year=orders)

@app.route("/orders/<int:year>/<int:month>")
def dashboard_ordersforyearandmonth(year, month):
    """Gets the orders for a particular year and month.
    """
    orders = clock.database.get_orders_for_year_and_month(year, month)

    return jsonify(orders_for_year_and_month=orders)

@app.route("/orders/count")
def order_count():
    """Gets a count of all orders.
    """
    count = clock.database.order_count

    return jsonify(order_count=count)

@app.route("/display/write")
def display_write():
    """Writes a message to the display.
    """
    message = request.args.get('message')
    LOGGER.info("Writing %s" % message)
    clock.display.write(message)
    return jsonify(result='Message Written!')

@app.route("/motor/turn")
def motor_turn():
    """Turns the motor.
    """
    wait_time = request.args.get('wait_time', 0, type=int)
    duration = request.args.get('duration', 0, type=int)
    LOGGER.info("Turning the motor with a wait time of %i and a duration of %i" % (wait_time, duration))
    clock.motor.turn(wait_time, duration)
    return jsonify(result='Motor Turned!')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8010, debug=True)
