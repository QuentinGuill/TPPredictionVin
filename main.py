from fastapi import FastAPI

from POST import predict
from GET import predict as predict2
from POST import retrain 
from GET import model 
from PUT import model as model2
from GET import description

import utils

app = FastAPI()

app.include_router(predict.router)
app.include_router(predict2.router)
app.include_router(retrain.router)
app.include_router(model.router)
app.include_router(model2.router)
app.include_router(description.router)

@app.get("/")
async def root():
    return {
    "app_version": utils.VERSION,
    "api_url_doc": utils.URL_DOC,
    "api_url_swagger": utils.URL_SWAGGER,
    "app_contacts": utils.CONTACTS
    }