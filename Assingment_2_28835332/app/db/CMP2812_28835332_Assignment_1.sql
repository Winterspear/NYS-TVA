Drop DATABASE if exists NewYorkTrafficViolations;
Drop user if exists 'SysAd'@'%';
Drop USER if exists 'Terminal'@'%';
Drop user if exists 'WebView'@'%';
CREATE DATABASE NewYorkTrafficViolations;
Use NewYorkTrafficViolations;

CREATE TABLE Address(
AddressID MEDIUMINT(50) NOT NULL AUTO_INCREMENT, 
AddressLine1 VARCHAR(30) NOT NULL, 
AddressLine2 VARCHAR(30), 
City VARCHAR(30) NOT NULL, 
State VARCHAR(30) NOT NULL, 
ZipCode VARCHAR(30) NOT NULL,
PRIMARY KEY (AddressID));

CREATE TABLE Driver (
DriverID MEDIUMINT(50) NOT NULL AUTO_INCREMENT, 
LastName VARCHAR(30) NOT NULL, 
FirstName VARCHAR(30) NOT NULL, 
Birthdate DATE NOT NULL, 
HeightFeet MEDIUMINT(12), 
HeightInches MEDIUMINT(12), 
Weight MEDIUMINT(12), 
EyeColor VARCHAR(30), 
DriversLicence VARCHAR(50) NOT NULL, 
AddressID MEDIUMINT(50),
PRIMARY KEY(DriverID), 
FOREIGN KEY (AddressID) REFERENCES Address (AddressID));

CREATE TABLE Vehicle (
VehicleID MEDIUMINT(50) NOT NULL AUTO_INCREMENT,
VIN VARCHAR(30) NOT NULL, 
Color VARCHAR(30), 
Make VARCHAR(30), 
AddressID MEDIUMINT(50) NOT NULL, 
manufactureYear YEAR, 
Design VARCHAR(30), 
DriverID MEDIUMINT(50) NOT NULL, 
PRIMARY KEY(VehicleID), 
FOREIGN KEY (AddressID) REFERENCES Address(AddressID),
FOREIGN KEY (DriverID) REFERENCES Driver(DriverID));

CREATE TABLE Officer (
PersonnelNumber MEDIUMINT(50) NOT NULL, 
FirstName VARCHAR(30) NOT NULL, 
LastName VARCHAR(30) NOT NULL, 
District MEDIUMINT(50) NOT NULL, 
Detachment MEDIUMINT(50) NOT NULL,
PRIMARY KEY (PersonnelNumber));

CREATE TABLE Violations (
ViolationID MEDIUMINT(50) NOT NULL AUTO_INCREMENT, 
ViolationDateTime DateTime NOT NULL, 
Distance MEDIUMINT(50) NOT NULL, 
Direction CHAR(1) NOT NULL, 
Landmark VARCHAR(30) NOT NULL, 
Road VARCHAR(30) NOT NULL, 
ViolationDetails VARCHAR(255) NOT NULL,
ActionPoint1 Bool NOT NULL,
Actionpoint2 BOOL NOT NULL,
Actionpoint3 BOOL NOT NULL,
PersonnelNumber MEDIUMINT(50) NOT NULL, 
DriverID MEDIUMINT(50) NOT NULL,
PRIMARY KEY (ViolationID),
FOREIGN KEY (PersonnelNumber) REFERENCES Officer(PersonnelNumber),
FOREIGN KEY (DriverID) REFERENCES Driver(DriverID));

CREATE TABLE Users (
userID MEDIUMINT(50) NOT NULL AUTO_INCREMENT,
forename VARCHAR(30) NOT NULL,
surname VARCHAR(30) NOT NULL,
email VARCHAR(30) NOT NULL UNIQUE,
password VARCHAR(300) NOT NULL,
driversLicence VARCHAR(30) NOT NULL,
dateOfBirth DATE NOT NULL,
phoneNumber VARCHAR(20) NOT NULL,
addressLine1 VARCHAR(30) NOT NULL,
addressLine2 VARCHAR(30),
city VARCHAR(30) NOT NULL,
state VARCHAR(30) NOT NULL,
zipCode VARCHAR(30) NOT NULL,
VIN VARCHAR(30) NOT NULL,
Role VARCHAR(30) NOT NULL,
PRIMARY KEY (userID));

CREATE USER 'SysAd' IDENTIFIED BY 'password';
CREATE USER 'Terminal' IDENTIFIED BY 'officer';
CREATE USER 'WebView' IDENTIFIED BY 'citizen';
GRANT ALL PRIVILEGES ON NewYorkTrafficViolations.* TO 'SysAd';
GRANT INSERT, SELECT ON NewYorkTrafficViolations.Address TO 'Terminal';
GRANT INSERT, SELECT ON NewYorkTrafficViolations.Driver TO 'Terminal';
GRANT INSERT, SELECT ON NewYorkTrafficViolations.Vehicle TO 'Terminal';
GRANT INSERT, SELECT ON NewYorkTrafficViolations.Violations TO 'Terminal';
GRANT SELECT ON NewYorkTrafficViolations.Address TO 'WebView';
GRANT SELECT ON NewYorkTrafficViolations.Driver TO 'WebView';
GRANT SELECT ON NewYorkTrafficViolations.Vehicle TO 'WebView';
GRANT SELECT ON NewYorkTrafficViolations.Violations TO 'WebView';

INSERT INTO NewYorkTrafficViolations.Officer
VALUES
(634, 'Josslyn', 'Abrahamson', 26, 30),
(409, 'Heath', 'Batts', 32, 12),
(208, 'Rhianna', 'Jackson', 1, 6);

INSERT INTO NewYorkTrafficViolations.Address(AddressLine1, AddressLine2, City, State, ZipCode)
VALUES
('1006 E','JEFFERSON RD', 'CHEYENNE', 'WY', '82007'),
('500 W', 'WASHINGTON ST', 'BALTIMORE', 'OH', '43105'),
('205', 'LEXINGTON AVE', 'MOUNT KISCO', 'NY', 10549),
('13400', 'BUFFALO RD', 'OAK HILLS', 'CA', '92344');

INSERT INTO NewYorkTrafficViolations.Driver(LastName, FirstName, Birthdate,  HeightFeet, HeightInches, Weight, EyeColor, DriversLicence)
VALUES
('WARDROBE', 'ROSY', '20021210', 5, 1, 121, 'BLUE', 12131231),
('JACOBSON', 'ANYA', '20060804', 5, 1, 153, 'BROWN', 223134),
('HERBERT', 'RUDYARD', '19441018', 5, 7, 186, 'BROWN', 34343342),
('ELLIOTT', 'KATEE', '20000303', 5, 4, 150, 'HAZEL', 4673154563),
('MILLWARD', 'DEEMER', '19630426', 5, 4, 175, 'GREY', 53446545633);
UPDATE NewYorkTrafficViolations.Driver
SET AddressID=1
WHERE Driver.DriverID = 1 OR Driver.DriverID = 3;
Update NewYorkTrafficViolations.Driver
SET AddressID=2
WHERE Driver.DriverID = 2;
Update NewYorkTrafficViolations.Driver
SET AddressID=3
WHERE Driver.DriverID = 4;
Update NewYorkTrafficViolations.Driver
SET AddressID=4
WHERE Driver.DriverID = 5;

INSERT INTO NewYorkTrafficViolations.Vehicle (VIN, Color, Make, AddressID, ManufactureYear, Design, DriverID)
VALUES
('WPOCA2A91ES130735', 'RED', 'FORD', 1, '2012', 'STATION WAGON', 1),
('WVGZZZ5NZJM131395', 'BLUE', 'VW', 2, '2012', 'CROSSOVER', 2),
('5YJSA1DG9DFP14705', 'GREEN', 'TOYOTA', 1, '1999', 'STATION WAGON', 3),
('1FABH41JXMN109186', 'BLACK', 'FORD', 3, '2018', 'HATCHBACK', 4),
('1FTFW1R6XBFB08616', 'BLACK', 'BMW', 4, '2024', 'LUXURY', 5);

INSERT INTO NewYorkTrafficViolations.Violations (ViolationDateTime, Distance, Direction, Landmark, Road, ViolationDetails, ActionPoint1, ActionPoint2, ActionPoint3, PersonnelNumber, DriverID)
VALUES
('2025-01-11 03:47:00', 1, 'E', 'Saratoga Springs', 'R-9', 'Drunk Driving',False, false, true, 409, 1),
('2025-11-06 17:25:00', 3, 'N', 'Lake George', '9N', 'Speeding', True, False, False, 208, 2),
('2025-06-08 16:43:00', 4, 'E', 'Lake George', '9N', 'Swerving Dangerously', True, False, False, 409, 3),
('2025-05-17 08:17:00', 2, 'S', 'Statue of Liberty', 'Off-Road', 'Unavailable', True, False, True, 634, 5),
('2025-03-10 12:06:00', 19, 'W', 'Saratoga Springs', 'I-87', 'Drunk Driving', False, False, True, 409, 1);

INSERT INTO NewYorkTrafficViolations.Users (forename, surname, email, password, driversLicence, dateOfBirth, phoneNumber, addressLine1, addressLine2, city, state, zipCode, VIN, Role)
Values ('Adam', 'Inn', 'Admin@gmail.com', '$argon2id$v=19$m=65536,t=3,p=4$FsK4F0KIsXauFaL0HoPwHg$GGU/fuHdMhIackANA3LuT50v5ywZtsHK8WuBttjEBgo', 'admin12221221', '19990101' , '01234567899', '1 Main Street', null, 'NY', 'NY', '10101010', '123123123163', 'admin')