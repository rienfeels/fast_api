from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")

def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/items/")

def read_items(skip: int = 0, limit: int = 10, q: str = None):
    if q:
        return {"skip": skip, "limit": limit, "q": q}
    else:
        return {"skip": skip, "limit": limit}
    

@app.get("/users/{user_id}")
def read_user_items(user_id):
    return {"user_id": user_id}

@app.get("/users/{user_id}/items/")
def read_user_items(user_id, skip, limit):
    return {"user_id": user_id, "skip": skip, "limit": limit}

