from fastapi import FastAPI
import uvicorn

app = FastAPI()

# http://localhost:8000/items/1
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

if __name__ == "__main__":
    uvicorn.run(app)

