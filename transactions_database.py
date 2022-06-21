# The point of this file is to store the transactions as they occur in the transaction mode,
# and the whole table will be sent off to all_transactions database to keep track of all transactions.
# Once that occurs, the data in this table will be deleted to be populated once again when a new transaction
# event begins.
import sqlite3

conn = sqlite3.connect('transactions.db')

c = conn.cursor()

# creating a database table at first run
c.execute("""CREATE TABLE IF NOT EXISTS transactions
(name text, sp real, date text, payment text, Qty)""")


def addData(item_name, sale_price, date, payment_type, qty):
    try:
        params = (item_name, sale_price, date, payment_type, qty)
        c.execute("INSERT INTO transactions VALUES (?, ?, ?, ?, ?)", params)
        conn.commit()
    except Exception as e:
        print('unable to insert', str(e))
        pass


def getData():
    c.execute("SELECT * FROM transactions")
    rows = c.fetchall()
    return list(rows)


def updatePaymentType(new_payment_type):
    params = (new_payment_type,)
    try:
        c.execute("UPDATE transactions SET payment = (?)", params)
        conn.commit()
    except Exception:
        pass


def deleteData():
    c.execute("DELETE FROM transactions")


conn.commit()
