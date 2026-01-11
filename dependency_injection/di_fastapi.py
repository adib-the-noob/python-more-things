from fastapi import FastAPI, Depends

class Database:
    def connect(self):
        return "Connected to database"
    def disconnect(self):
        return "Disconnected from database"

def get_db():
    db = Database()
    try:
        yield db.connect()
    finally:    
        db.disconnect()

app = FastAPI()

@app.get("/data")
def read_data(db=Depends(get_db)):
    return {"db_status": db}