from datetime import datetime
import logging
import sqlite3 as db


class Database(object):
    """This is a class that represents the database.
    """

    def __init__(self, configuration):
        """Create a new instance of the database class.
        """
        self._configuration = configuration
        self._logger = logging.getLogger(__name__)

        self._db_file = self._configuration.database_file_name
        self._schema_file = self._configuration.schema_file_name

        self._create_schema()

    @property
    def chart_data(self):
        """Gets the data for the chart.
        """
        data = self.get_orders_for_year(int(datetime.today().year))

        # Okay, this is a bit goofy. Normally we wouldn't concern ourselves with styling in a place like this, but...

        chart_data = {
            "labels": ["January",
                       "February",
                       "March",
                       "April",
                       "May",
                       "June",
                       "July",
                       "August",
                       "September",
                       "November",
                       "December"],
            "datasets": [{
                "label": "Orders",
                "fillColor": "#FF6600",
                "strokeColor": "#FFFFFF",
                "pointColor": "rgba(220,220,220,1)",
                "pointStrokeColor": "#FFFFFF",
                "pointHighlightFill": "#FFFFFF",
                "pointHighlightStroke": "rgba(220,220,220,1)",
                "data": data
            }]
        }

        return chart_data

    @property
    def orders(self):
        """Gets all orders.
        """
        con = db.connect(self._db_file)

        con.row_factory = db.Row

        with con:
            cur = con.cursor()

            cur.execute("SELECT order_year, order_month, order_count FROM Orders ORDER BY order_year, order_month")

            rows = cur.fetchall()

            result = self._row_to_dict(rows)

            self._logger.info("Orders for Year: %s" % result)

            return result

    @property
    def order_count(self):
        """Gets the order count.
        """
        con = db.connect(self._db_file)

        with con:
            cur = con.cursor()

            cur.execute("SELECT SUM(order_count) FROM Orders")

            row = cur.fetchone()

            if row is None:
                result = 0
            else:
                if row[0] is None:
                    result = 0
                else:
                    result = row[0]

            return result

    def get_orders_for_year_and_month(self, order_year, order_month):
        """Gets the total number of orders for a particular month.
        """
        con = db.connect(self._db_file)

        with con:
            cur = con.cursor()

            cur.execute("SELECT order_count FROM Orders WHERE order_year = ? AND order_month = ?",
                        (order_year, order_month))

            row = cur.fetchone()

            if row is None:
                result = 0
            else:
                if row[0] is None:
                    result = 0
                else:
                    result = row[0]

            return result

    def get_orders_for_year(self, order_year):
        """Gets the order totals for a particular year.
        """

        con = db.connect(self._db_file)

        con.row_factory = db.Row

        with con:
            cur = con.cursor()

            cur.execute("SELECT order_count FROM Orders WHERE order_year = %s ORDER BY order_month" % order_year)

            rows = cur.fetchall()

            result = self._row_to_dict(rows)

            self._logger.info("Orders for Year: %s" % result)

            return result

    def record_order(self, order_year, order_month):
        """Records a new order into the database.
        """
        self._logger.info("Inserting order")

        con = db.connect(self._db_file)

        with con:
            cur = con.cursor()

            current_order_count = self.get_orders_for_year_and_month(order_year, order_month)

            order_count = self.get_orders_for_year_and_month(order_year, order_month) + 1

            if current_order_count is 0:
                cur.execute("INSERT INTO Orders (order_year, order_month, order_count) VALUES(?, ?, ?)",
                            (order_year, order_month, order_count))
            else:
                cur.execute("UPDATE Orders SET order_count = ? WHERE order_year = ? AND order_month = ?",
                            (order_count, order_year, order_month))

    def _create_schema(self):
        """Creates the table we need.
        """
        con = db.connect(self._db_file)

        with con:
            self._logger.info('Creating schema')

            with open(self._schema_file, 'rt') as f:
                schema = f.read()
                con.executescript(schema)

    @staticmethod
    def _row_to_dict(rows):
        """Turns a list with sqlite3.Row objects into a dictionary
        """
        d = {}

        for i, row in enumerate(rows):
            l = []

            for col in range(0, len(row)):
                l.append(row[col])

            d[i] = l

        return d
