import sqlite3

db = sqlite3.connect("server.db")
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS my_db(
    login TEXT,
    password TEXT,
    cash BIGINT
    
)""")
db.commit()
user_login = "seregatheone"
user_password = "pass"
cash = 1234
sql.execute("SELECT login FROM `my_db` WHERE 1")
if sql.fetchall()is None:
    sql.execute(f"INSERT INTO my_db VALUES (?,?,?)",(user_login,user_password,cash))
    db.commit()
else:
    print(1234)