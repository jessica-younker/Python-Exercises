import sys
import sqlite3
from datetime import datetime
from time import time

class Amazon:
  '''A simplified class to buy stock in Amazon'''

  def buy_amazon(self, quantity, purchase_price):
    '''Allows a user to purchase Amazon stock
    Method arguments
    ----------------
      quantity -- (integer) The number of stocks to purchase
      purchase_price -- (real) The price at which the stocks were purchased
    '''
    with sqlite3.connect('example.db') as conn:
        # factory worker of relational db. interface btw db and code
      c = conn.cursor()

      try:
        # triple quotes allow you to include line break in following sql stmt w/o python complaining
        c.execute("""create table stocks
          (date text, trans text, symbol text, qty integer, price real)""")
      except sqlite3.OperationalError:
        pass

      timestamp = time()
      date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
      trans = "BUY"
      symbol = "AMZN"
      # ? are placeholders for sqllite3 adapter
      c.execute("insert into stocks values (?, ?, ?, ?, ?)",
                    (date, trans, symbol, quantity, purchase_price))
      # must do commit to save to db
      conn.commit()

  def query_all_amazon(self):
    '''Query and print all of the transactions for purchased Amazon stocks
    Method arguments
    ----------------
      n/a
    '''

    with sqlite3.connect('example.db') as conn:
      c = conn.cursor()

      c.execute("select * from stocks where trans=? and symbol=?", ("BUY", "AMZN"))
      # don't need to commit after this because only reading, not writing
      print(c.fetchall())

  def query_latest_amazon(self):
    '''Query and print last transaction
    Method arguments
    ----------------
      n/a
    '''

    with sqlite3.connect('example.db') as conn:
      c = conn.cursor()

      c.execute("select * from stocks where trans=? and symbol=? order by date desc", ("BUY", "AMZN"))
      print(c.fetchone())


  def clear_database(self):
    '''Deletes all transactions from the database
    Method arguments
    ----------------
      n/a
    '''
    with sqlite3.connect('example.db') as conn:
      c = conn.cursor()

      c.execute("delete from stocks")
      conn.commit()



if __name__ == "__main__":
  amz = Amazon()
  # amz.clear_database()
  amz.buy_amazon(sys.argv[1], sys.argv[2])
  amz.query_latest_amazon()
  amz.query_all_amazon()