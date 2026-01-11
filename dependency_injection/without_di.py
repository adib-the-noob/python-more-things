class Database:
    def connect(self):
        # print("Database connected")
        return "Connected to database"
    

class Service:
    def __init__(self) -> None:
        self.database = Database()

    def get_data(self):
        return self.database.connect() # Tightly coupled to Database class
    
db_service = Service()
print(db_service.get_data())