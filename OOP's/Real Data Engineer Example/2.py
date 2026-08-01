class Database:

    def connect(self):
        print("Connecting...")

db = Database()
db.connect()

# Now for MySQL:

class MySQL(Database):

    def connect(self):
        print("Connected to MySQL")

mysql = MySQL()
mysql.connect()