DROP TABLE IF EXISTS Computer;

Create Table Employee (
    EmployeeID Integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    DepartmentID Integer NOT NULL ,
    Title Text NOT NULL,
    FOREIGN KEY(DepartmentID) References Department(DepartmentID)
);

Create Table EmployeeComputer (
    EmComID Integer NOT NULL Primary Key Autoincrement,
    EmployeeID Integer NOT NULL,
    ComputerID Integer NOT NULL,
    Foreign Key(ComputerID) References Computer(ComputerID),
    Foreign Key(EmployeeID) References Employee(EmployeeID)
);

Create Table Computer (
    ComputerID Integer Not Null Primary Key Autoincrement,
    Purchase_Date Date Not Null,
    Decommission_Date Date Not Null
);

Create Table Department (
    DepartmentID Integer Not Null Primary Key Autoincrement,
    Expense Budget Text NOT NULL
);

Create Table EmployeeTrainingProg (
    TrainingProgramID Integer Not Null Primary Key Autoincrement,
    EmployeeID Integer Not Null,
    Foreign Key(EmployeeID) References Employee(EmployeeID)
);

Create Table TrainingProgram (
    TrainingProgramID Integer Not Null Primary Key Autoincrement,
    Start_Date Text Not Null,
    End_Date Text Not Null, 
    Maximum_Occupancy Text Not Null
);

Create Table OrderTable (
    OrderID Integer Not Null Primary Key Autoincrement,
    CustomerID Text Not Null,
    PaymentTypeID Text Not Null,
    Foreign Key(CustomerID) References Customer(CustomerID),
    Foreign Key(PaymentTypeID) References PaymentType(PaymentTypeID)
);

Create Table PaymentType (
    PaymentTypeID Integer Not Null Primary Key Autoincrement,
    Account_Number Integer Not Null
);

Create Table OrderProduct (
    OrderProductID Integer Not Null Primary Key Autoincrement,
    ProductID Text Not Null,
    OrderID Text Not Null,
    Foreign Key(ProductID) References Product(ProductID),
    Foreign Key(OrderID) References OrderTable(OrderID)
);

Create Table ProductType (
    ProductTypeID Integer Not Null Primary Key Autoincrement,
    Category_Name Text Not Null
);

Create Table Product (
    ProductID Integer Not Null Primary Key Autoincrement,
    Price Text Not Null,
    Title Text Not Null,
    Description Text Not Null,
    CustomerID Text Not Null,
    Foreign Key(CustomerID) References Customer(CustomerID)
);

Create Table Customer (
    CustomerID Integer Not Null Primary Key Autoincrement,
    First_Name Text Not Null,
    Last_Name Text Not Null,
    Status Integer Not Null,
    Date_Created
);

INSERT INTO EmployeeComputer VALUES (null, 1, 2);
INSERT INTO EmployeeComputer VALUES (null, 2, 4);
INSERT INTO EmployeeComputer VALUES (null, 3, 6);

INSERT INTO Computer VALUES (null, "2012-12-12", "2016-12-12");
INSERT INTO Computer VALUES (null, 2012-12-12, 2016-12-12);
INSERT INTO Computer VALUES (null, 2012-12-12, 2016-12-12);

INSERT INTO Employee VALUES (null, 5, "Supervisor");
INSERT INTO Employee VALUES (null, 7, "Staff");
INSERT INTO Employee VALUES (null, 9, "Developer");

INSERT INTO Department VALUES (null, 2000);
INSERT INTO Department VALUES (null, 2555);
INSERT INTO Department VALUES (null, 2444);

INSERT INTO EmployeeTrainingProg VALUES (null, 13);
INSERT INTO EmployeeTrainingProg VALUES (null, 9);
INSERT INTO EmployeeTrainingProg VALUES (null, 22);
\*
INSERT INTO TrainingProgram VALUES (null, 1, 2);
INSERT INTO TrainingProgram VALUES (null, 1, 2);
INSERT INTO TrainingProgram VALUES (null, 1, 2);

INSERT INTO Order_Table VALUES (null, 1, 2);
INSERT INTO Order_Table VALUES (null, 1, 2);
INSERT INTO Order_Table VALUES (null, 1, 2);

INSERT INTO OrderProduct VALUES (null, 1, 2);
INSERT INTO OrderProduct VALUES (null, 1, 2);
INSERT INTO OrderProduct VALUES (null, 1, 2);

INSERT INTO PaymentType VALUES (null, 1, 2);
INSERT INTO PaymentType VALUES (null, 1, 2);
INSERT INTO PaymentType VALUES (null, 1, 2);

INSERT INTO ProductType VALUES (null, 1, 2);
INSERT INTO ProductType VALUES (null, 1, 2);
INSERT INTO ProductType VALUES (null, 1, 2);

INSERT INTO Product VALUES (null, 1, 2);
INSERT INTO Product VALUES (null, 1, 2);
INSERT INTO Product VALUES (null, 1, 2);

INSERT INTO Customer VALUES (null, 1, 2);
INSERT INTO Customer VALUES (null, 1, 2);
INSERT INTO Customer VALUES (null, 1, 2);
\*
    
