import uvicorn
from fastapi import FastAPI
from database import SessionLocal, engine, Base 
from routers import user as User_router
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(User_router.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000) 