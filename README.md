# supermarket_analysis

## Supermarket Sales Analysis

This project performs exploratory data analysis (EDA) on a supermarket sales dataset using Python. It generates insights and visualizations to understand sales patterns, customer behavior, and product performance.

## Project Structure

```
├── supermarket_analysis.py   # Main analysis script
├── Testing.py                # Data validation & testing script
├── supermarket_sales.csv    # Dataset
└── README.md                # Project documentation
```

## Dataset Description

The dataset contains sales transactions from a supermarket, including :-

- Invoice ID
- Branch & City
- Customer Type (Member / Normal)
- Gender
- Product Line
- Unit Price & Quantity
- Total Sales & Tax
- Date & Time
- Payment Method
- Rating

## Features & Analysis

### Data Processing
- Loads dataset using pandas
- Converts Date column to datetime format
- Extracts :- 
    - Month
    - Day of the week


## Key Insights Generated

1. Sales Overview
      - Total Revenue
      - Average Customer Rating

2. Sales by Branch
      - Compares revenue across different branches
  
3. Product Line Performance
      - Identifies best and worst performing product categories
  
4. Payment Method Distribution
      - Analyzes customer payment preferences
  
5. Customer Type & Gender Analysis
      - Sales breakdown by :
        
         - Member vs Normal customers
         - Male vs Female customers
       
6. Product Ratings
      - Average rating for each product line
  
7. Monthly Sales Trend
      - Sales trend across January, February, and March
  

## Testing & Validation (Testing.py)

The testing script ensures :

- Dataset loads correctly
- Missing values are identified
- Date conversion is validated
- Statistical summary of numerical data
- Re-runs all visualizations for verification


## Requirements

Install required libraries before running :-

```
pip install pandas matplotlib seaborn
```


## How to Run

Run Analysis :-

```
python supermarket_analysis.py
```

Run Testing :-

```
python Testing.py
```


## Sample Visualizations

The project generates :-

- Bar charts (sales by branch, product line)
- Count plots (payment methods)
- Stacked bar charts (customer type & gender)
- Line plots (monthly trends)


##  Insights You Can Derive

- Which branch generates the most revenue
- Most popular product categories
- Preferred payment methods
- Customer purchasing patterns
- Monthly sales trends


## Future Improvements

- Add interactive dashboards (e.g., Plotly / Power BI)
- Perform predictive analysis (sales forecasting)
- Deploy as a web app using Flask/Streamlit
- Include more advanced KPIs


## License

This project is open-source and free to use for learning purposes.
