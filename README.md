# Sales Data Cleaning and Analysis

Cleaning a messy sales dataset and looking at revenue with Python (Pandas, NumPy, Matplotlib).

The data is synthetic. `make_data.py` creates it and adds problems on purpose: duplicate rows, mixed date formats, messy city names, missing values and wrong prices.

## What I did
- removed 30 duplicate orders
- fixed the two date formats (YYYY-MM-DD and DD/MM/YYYY)
- fixed city names (extra spaces, upper and lower case)
- treated 3 wrong prices (negative or too big) as missing
- filled missing prices with the median of the same product and missing quantities with the median
- left missing ratings empty
- added revenue and month columns
- made 4 charts

## Results (600 clean orders)
- total revenue: $621,130
- average order value: $1,035
- best month: October 2025
- top product: Laptop
- top city: Lahore

## Files
| File | Description |
|---|---|
| `make_data.py` | creates the fake messy sales data |
| `sales_analysis.ipynb` | notebook with cleaning, analysis and charts |
| `sales_raw_messy.csv` | data before cleaning |
| `sales_clean.csv` | data after cleaning |
| `chart1_monthly_revenue.png` | monthly revenue |
| `chart2_revenue_by_product.png` | revenue by product |
| `chart3_revenue_by_city.png` | revenue by city |
| `chart4_avg_rating.png` | average rating by product |

## How to run
```
pip install pandas numpy matplotlib jupyter
python make_data.py
jupyter notebook
```
Then open `sales_analysis.ipynb` and run all cells.
