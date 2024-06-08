import sqlite3 
  
# Connecting to sqlite 
conn = sqlite3.connect('food.db') 
  
# Now we need to Create a cursor object using the cursor() method 
cursor = conn.cursor() 

#creation of users table
Users_table="""CREATE TABLE Users (
    UserID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Email TEXT UNIQUE NOT NULL,
    Phone TEXT UNIQUE NOT NULL,
    Address TEXT NOT NULL
);"""
cursor.execute(Users_table)

#Insertion of records to users table
cursor.execute('''
INSERT INTO Users VALUES (1, 'John Doe', 'john@example.com', '123-456-7890', '123 Main St');
''')
cursor.execute('''
INSERT INTO Users VALUES (2, 'Jane Smith', 'jane@example.com', '987-654-3210', '456 Oak Ave');
''')
cursor.execute('''
INSERT INTO Users VALUES (3, 'Michael Johnson', 'michael@example.com', '555-123-4567', '789 Elm St');
''')
cursor.execute('''
INSERT INTO Users VALUES (4, 'Emily Davis', 'emily@example.com', '111-222-3333', '456 Pine Rd');
''')
cursor.execute('''
INSERT INTO Users VALUES (5, 'Sarah Wilson', 'sarah@example.com', '333-555-7777', '1010 Broadway');
''')

#creation of restaurent table
Restaurent_table="""CREATE TABLE Restaurant (
    RestaurantID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    CuisineType TEXT,
    Location TEXT NOT NULL,
    ContactInfo TEXT NOT NULL
);
"""
cursor.execute(Restaurent_table)

#Insertion of records to restaurent table
cursor.execute('''
INSERT INTO Restaurant VALUES (101, 'Pizza Palace', 'Italian', '789 Elm St', 'info@pizzapalace.com');
''')
cursor.execute('''
INSERT INTO Restaurant VALUES (102, 'Burger Barn', 'American', '456 Maple Ave', 'info@burgerbarn.com');
''')
cursor.execute('''
INSERT INTO Restaurant VALUES (103, 'Sushi House', 'Japanese', '123 Sakura Rd', 'info@sushihouse.com');
''')
cursor.execute('''
INSERT INTO Restaurant VALUES (104, 'Taco Town', 'Mexican', '777 Jalapeno St', 'info@tacotown.com');
''')
cursor.execute('''
INSERT INTO Restaurant VALUES (105, 'Curry Corner', 'Indian', '555 Spice Ave', 'info@currycorner.com');
''')

#creation of order table
Order_table="""CREATE TABLE Orders (
    OrderID INTEGER PRIMARY KEY,
    UserID INTEGER,
    RestaurantID INTEGER,
    OrderDateTime TEXT NOT NULL,
    TotalAmount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (RestaurantID) REFERENCES Restaurant(RestaurantID)
);
"""
cursor.execute(Order_table)

#Insertion of records to orders table
cursor.execute('''
INSERT INTO Orders VALUES (10001, 1, 101, '2023-10-04 12:00:00', 27.98);
''')
cursor.execute('''
INSERT INTO Orders VALUES (10002, 2, 102, '2023-10-04 12:30:00', 16.98);
''')
cursor.execute('''
INSERT INTO Orders VALUES (10003, 3, 103, '2023-10-04 13:00:00', 39.98);
''')
cursor.execute('''
INSERT INTO Orders VALUES (10004, 4, 104, '2023-10-04 13:30:00', 13.98);
''')
cursor.execute('''
INSERT INTO Orders VALUES (10005, 5, 105, '2023-10-04 14:00:00', 25.98);
''')

#creation of order_items table
Order_items_table="""CREATE TABLE OrderItems (
    OrderItemID INTEGER PRIMARY KEY,
    OrderID INTEGER,
    MenuID INTEGER,
    Quantity INTEGER NOT NULL
    
); """
cursor.execute(Order_items_table)

#Insertion of records to ordered items table
cursor.execute('''
INSERT INTO OrderItems VALUES (5001, 10001, 1001, 1);
''')
cursor.execute('''
INSERT INTO OrderItems VALUES (5002, 10001, 1002, 1);
''')
cursor.execute('''
INSERT INTO OrderItems VALUES (5003, 10002, 2001, 2);
''')
cursor.execute('''
INSERT INTO OrderItems VALUES (5004, 10003, 3001, 1);
''')
cursor.execute('''
INSERT INTO OrderItems VALUES (5005, 10003, 3002, 1);
''')

#creation of delivery boy table
delivery_boy_table="""CREATE TABLE DeliveryDriver (
    DeliveryDriverID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    VehicleDetails TEXT,
    ContactInfo TEXT NOT NULL
);
"""
cursor.execute(delivery_boy_table)

#Insertion of records to delivery boy details table
cursor.execute('''
INSERT INTO DeliveryDriver VALUES (501, 'Sam Johnson', 'Car - ABC123', 'sam@example.com');
''')
cursor.execute('''
INSERT INTO DeliveryDriver VALUES (502, 'Emily Davis', 'Bike - XYZ789', 'emily@example.com');
''')
cursor.execute('''
INSERT INTO DeliveryDriver VALUES (503, 'Michael Brown', 'Car - DEF456', 'michael@example.com');
''')
cursor.execute('''
INSERT INTO DeliveryDriver VALUES (504, 'Lisa Smith', 'Motorcycle - MNO789', 'lisa@example.com');
''')
cursor.execute('''
INSERT INTO DeliveryDriver VALUES (505, 'Daniel Wilson', 'Car - GHI123', 'daniel@example.com');
''')

#creation of delivery status table
Delivery_table="""CREATE TABLE Delivery (
    DeliveryID INTEGER PRIMARY KEY,
    OrderID INTEGER UNIQUE,
    DriverID INTEGER,
    Status TEXT NOT NULL,
    DeliveryDateTime TEXT,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (DriverID) REFERENCES DeliveryDriver(DriverID)
);"""

cursor.execute(Delivery_table)

#Insertion of records to delivery  table
cursor.execute('''
INSERT INTO Delivery VALUES (1001, 10001, 501, 'Delivered', '2023-10-04 12:45:00');
''')
cursor.execute('''
INSERT INTO Delivery VALUES (1002, 10002, 502, 'In Transit', NULL);
''')
cursor.execute('''
INSERT INTO Delivery VALUES (1003, 10003, 503, 'Delivered', '2023-10-04 13:15:00');
''')
cursor.execute('''
INSERT INTO Delivery VALUES (1004, 10004, 504, 'Delivered', '2023-10-04 13:30:00');
''')
cursor.execute('''
INSERT INTO Delivery VALUES (1005, 10005, 505, 'In Transit', NULL);
''')

# Tables that we used are: STUDENT, Users, Restaurant, Orders, OrderItems, Delivery

tables = [ "Users", "Restaurant", "Orders", "OrderItems","DeliveryDriver","Delivery"]

for table in tables:
    print(f"Data Inserted in the {table} table:")
    data = cursor.execute(f"SELECT * FROM {table}")
    for row in data:
        print(row)

conn.commit() 

conn.close()


