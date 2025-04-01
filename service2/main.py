
from fastapi import FastAPI, Request

app = FastAPI(title="Service 2")


@app.get("/")
async def root():
    return {"message": "Hello from Service 2!"}


@app.get("/service2/orders")
async def get_orders():
    return {"orders": [{"id": 1, "item": "Book"}, {"id": 2, "item": "Pen"}], "service": "Service 2"}


@app.get("/service2/customers")
async def get_customers():
    return {"customers": ["David", "Eve", "Frank"], "service": "Service 2"}


@app.get("/info")
async def info(request: Request):
    client_host = request.client.host
    headers = dict(request.headers)
    return {
        "service": "Service 2",
        "client_ip": client_host,
        "headers": headers
    }
