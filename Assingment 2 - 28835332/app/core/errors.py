class addressNotFound(Exception):
    def __init__(self, addressID: int):
        self.addressID = addressID

class driverNotFound(Exception):
    def __init__(self, driverID: int):
        self.driverID = driverID

class licenceStateNotFound(Exception):
    def __init__(self, licenceStateID: int):
        self.licenceStateID = licenceStateID

class vehicleNotFound(Exception):
    def __init__(self, vehicleID: int):
        self.vehicleID = vehicleID

class driverNotFound(Exception):
    def __init__(self, driverID: int):
        self.driverID = driverID

class officerNotFound(Exception):
    def __init__(self, personnelID: int):
        self.personnelID = personnelID

class DatabaseConnectionError(Exception):
    def __init__(self, message: str = "Database connection failed"):
        self.message = message

class DatabaseQueryError(Exception):
    def __init__(self, message: str = "Database query failed"):
        self.message = message

class InvalidAPIKeyError(Exception):
    def __init__(self, message: str = "Missing or Invalid API key"):
        self.message = message