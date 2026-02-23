from fastapi import FastAPI, request
from app.api import drivers, officers, vehicles, violations, addresses, licenceStates, auth
from app.db.init_db import init_db
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="New York State Traffic Violation API", version="1.0.0")

init_db()


app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(drivers.router, prefix="/drivers", tags=["Drivers"])
app.include_router(officers.router, prefix="/officers", tags=["Officers"])
app.include_router(vehicles.router, prefix="/vehicles", tags=["Vehicles"])
app.include_router(violations.router, prefix="/violations", tags=["Violations"])
app.include_router(addresses.router, prefix="/addresses", tags=["Addresses"])
app.include_router(licenceStates.router, prefix="/licence-states", tags=["Licence States"])

@app.get("/")
def root():
    return {"message": "Welcome to the New York State Traffic Violation API!"}