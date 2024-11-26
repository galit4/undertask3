from fastapi import FastAPI
from api import helloworld

app = FastAPI()
app.include_router(helloworld.router)

#test