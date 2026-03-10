import csv
import random
from datetime import datetime, timedelta
import os

output_dir = r"C:\Users\Dell\.gemini\antigravity\scratch\SupplyChainProject\Data"
os.makedirs(output_dir, exist_ok=True)

random.seed(42)

# 1. Dim_Suppliers
suppliers = []
regions = ['North America', 'Europe', 'Asia', 'South America']
for i in range(1, 21):
    suppliers.append({
        'SupplierID': f'S{str(i).zfill(3)}',
        'SupplierName': f'Supplier_{chr(65+(i%26))}{i}',
        'Region': random.choice(regions),
        'ReliabilityRating': round(random.uniform(0.7, 0.99), 2)
    })

with open(os.path.join(output_dir, 'dim_suppliers.csv'), 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['SupplierID', 'SupplierName', 'Region', 'ReliabilityRating'])
    writer.writeheader()
    writer.writerows(suppliers)

# 2. Dim_Products
products = []
categories = ['Electronics', 'Clothing', 'Home Goods', 'Industrial', 'Medical']
for i in range(1, 101):
    products.append({
        'ProductID': f'P{str(i).zfill(4)}',
        'ProductName': f'Product_{i}',
        'Category': random.choice(categories),
        'UnitCost': round(random.uniform(10.0, 500.0), 2)
    })

with open(os.path.join(output_dir, 'dim_products.csv'), 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['ProductID', 'ProductName', 'Category', 'UnitCost'])
    writer.writeheader()
    writer.writerows(products)

# 3. Fact_Inventory
inventory = []
warehouses = ['W01', 'W02', 'W03', 'W04']
for p in products:
    inventory.append({
        'WarehouseID': random.choice(warehouses),
        'ProductID': p['ProductID'],
        'CurrentStockLevel': random.randint(50, 1000),
        'ReorderPoint': random.randint(100, 300),
        'MaxCapacity': random.randint(800, 2000)
    })

with open(os.path.join(output_dir, 'fact_inventory.csv'), 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['WarehouseID', 'ProductID', 'CurrentStockLevel', 'ReorderPoint', 'MaxCapacity'])
    writer.writeheader()
    writer.writerows(inventory)

# 4. Fact_Orders
orders = []
num_orders = 5000
start_date = datetime(2023, 1, 1)

for i in range(1, num_orders + 1):
    order_date = start_date + timedelta(days=random.randint(0, 365))
    supplier = random.choice(suppliers)
    expected_lead = random.randint(5, 15)
    expected_delivery = order_date + timedelta(days=expected_lead)
    
    # Calculate delay based on supplier reliability
    delay_chance = 1.0 - supplier['ReliabilityRating']
    if random.random() < delay_chance + 0.1:
        delay_days = random.randint(1, 10)
        actual_delivery = expected_delivery + timedelta(days=delay_days)
    else:
        actual_delivery = expected_delivery - timedelta(days=random.randint(0, 2))
        
    orders.append({
        'OrderID': f'ORD{str(i).zfill(5)}',
        'OrderDate': order_date.strftime('%Y-%m-%d'),
        'ExpectedDeliveryDate': expected_delivery.strftime('%Y-%m-%d'),
        'ActualDeliveryDate': actual_delivery.strftime('%Y-%m-%d'),
        'ProductID': random.choice(products)['ProductID'],
        'SupplierID': supplier['SupplierID'],
        'OrderQty': random.randint(10, 500),
        'IsLate': 1 if actual_delivery > expected_delivery else 0
    })

# Sort by order date
orders.sort(key=lambda x: x['OrderDate'])

with open(os.path.join(output_dir, 'fact_orders.csv'), 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=[
        'OrderID', 'OrderDate', 'ExpectedDeliveryDate', 'ActualDeliveryDate',
        'ProductID', 'SupplierID', 'OrderQty', 'IsLate'
    ])
    writer.writeheader()
    writer.writerows(orders)

print(f"Data successfully generated at {output_dir}")
