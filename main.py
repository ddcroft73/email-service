from fastapi import FastAPI
import logging
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from routes import email

app = FastAPI()

static_directory: str ="static"
app.mount("/static", StaticFiles(directory=static_directory), name="static")

app.include_router(email.router)

@app.get('/', response_class=RedirectResponse)  #  response_class=RedirectResponse, include_in_schema=False
async def index():
    return RedirectResponse(url='/static/index.html')
  