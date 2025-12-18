# Task 6 – Sales Trend Analysis Using SQL

## Objective
The objective of this task is to analyze sales trends by calculating **monthly revenue** and **monthly order volume** using SQL aggregation functions.

---

## Tools Used
- SQL Server (SSMS)
- SQL

---

## Dataset
**File:** `sales_orders.csv`

### Dataset Columns:
- `order_id` – Unique identifier for each order  
- `order_date` – Date of the order  
- `amount` – Order amount (sales value)  
- `product_id` – Identifier for the product  

The dataset contains sales data across multiple months, making it suitable for trend analysis.

---

## Analysis Performed
- Grouped sales data by **year and month**
- Calculated **monthly revenue** using `SUM(amount)`
- Calculated **monthly order volume** using `COUNT(order_id)`
- Identified **top-performing months** based on revenue
- Analyzed overall sales growth trend

---

## Key Insights
- Sales show a steady increase over time
- Certain months recorded higher revenue and order volume
- Order volume growth aligns closely with revenue trends
- Monthly aggregation helps identify seasonal patterns

---

## Files Included
- `sales_orders.csv` – Dataset used for analysis  
- `sales_trend.sql` – SQL queries for trend analysis  
- `screenshots/` – Query results screenshots  
- `README.md` – Task documentation  

---

## Outcome
This task demonstrates the use of SQL aggregation functions, `GROUP BY`, and date-based analysis to extract meaningful business insights from sales data.
