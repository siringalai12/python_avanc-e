from fastapi import FastAPI
from .routers import students

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the students management FastAPI application!"}

# Inclure les routes
app.include_router(students.router)
