from fastapi import FastAPI, Request
from app.api import drivers, officers, vehicles, violations, addresses, auth, users
from app.db.init_db import init_db
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, List


app = FastAPI(title="New York State Traffic Violation API", version="1.0.0")

init_db()


app.include_router(auth.router)
app.include_router(drivers.router)
app.include_router(officers.router)
app.include_router(vehicles.router)
app.include_router(violations.router)
app.include_router(addresses.router)
print("REGISTERING USERS ROUTER")
app.include_router(users.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to the New York State Traffic Violation API!"}