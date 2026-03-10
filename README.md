# Supply Chain Analytics Dashboard 

## 📌 Project Overview
The goal of this project is to analyze supply chain data to identify potential shipping delays and track inventory levels. This dashboard was built to practice data modeling and data visualization in Power BI.

This project features a basic Supply Chain Dashboard designed to track vendor reliability, monitor inventory stock levels, and provide a clear view of order fulfillment.

## 📊 Dashboard Pages
*   **Overview Dashboard:** Basic KPIs including Total Orders, On-Time Delivery %, and Total Inventory Value.
*   **Supplier Performance:** A bar chart of late shipments and a table ranking suppliers by reliability.
*   **Logistics Timeline:** A line chart showing delivery time trends over the year.
*   **Inventory Check:** A table showing current stock levels with simple conditional formatting for potential overstock.

## 🛠️ Data Modeling
The data was modeled using a basic **Star Schema** to connect the tables:
*   **Fact Tables:** `fact_orders` (shipping data), `fact_inventory` (stock levels).
*   **Dimension Tables:** `dim_suppliers` (vendor details), `dim_products` (product categories).
*   **Date Table:** A simple calendar table created using DAX `CALENDAR()`.

## 📈 Key Skills Practiced
*   **Data Modeling:** Connecting tables using 1-to-Many relationships.
*   **Basic DAX:** Writing simple `CALCULATE()`, `DIVIDE()`, and `SUM()` formulas.
*   **Calculated Columns:** Using `DATEDIFF()` to find delivery times.
*   **Data Visualization:** Adding standard slicers (filters) and basic conditional formatting.

## 🗂️ Data Sources
The dashboard is built upon a custom generated relational dataset containing 5,000 randomized orders, complete with simulated shipping delays, supplier reliability variations, and inventory capacity constraints. The data is available in the `/Data` directory.
