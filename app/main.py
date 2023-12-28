from fastapi import FastAPI
app = FastAPI()
from .models import models
from .database.database import engine
from .api import auth,lawyer

# Define a route

models.Base.metadata.create_all(engine)
app.include_router(lawyer.router)
app.include_router(auth.router)




