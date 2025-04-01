from fastapi import FastAPI, Request

app = FastAPI(title="Service 1")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello from service 1"}


@app.get("/service1/users")
async def get_users():
    return {"users": ["Alice", "Bob", "Charlie"], "service": "Service 1"}


@app.get("/service1/products")
async def get_products():
    return {"products": ["Laptop", "Phone", "Tablet"], "service": "Service 1"}


@app.get("/info")
async def info(request: Request):
    client_host = request.client.host
    headers = dict(request.headers)
    return {
        "service": "Service 1",
        "client_ip": client_host,
        "headers": headers
    }
