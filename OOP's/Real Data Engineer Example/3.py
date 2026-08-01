# For PostgreSQL:
class Database:

    def connect(self):
        print("Connecting...")

db = Database()
db.connect()

#####################################################
class PostgreSQL(Database):

    def connect(self):
        print("Connected to PostgreSQL")

PostgreSQL = PostgreSQL()
PostgreSQL.connect()