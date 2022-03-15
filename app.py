from fastapi import FastAPI
from routes.user import user

app = FastAPI()

@app.get('/')
def get_raiz():
    return {"Holiii aqui no hay ni %$& dirigete a /docs"}

app.include_router(user)