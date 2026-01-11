class Database:
    def connect(self):
        # print("Database connected")
        return "Connected to database"
    

class Service:
    def __init__(self) -> None:
        self.database = Database()

    def get_data(self, db: Database):
        return db.connect() # Now accepts Database instance as parameter
    
db_service = Service()
print(db_service.get_data(Database()))