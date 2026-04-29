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


## Screenshots

<img width="1089" height="605" alt="Output 1" src="https://github.com/user-attachments/assets/25566fb1-9d2e-41cf-970b-3bff16c79d87" />

<img width="1195" height="683" alt="Output 2" src="https://github.com/user-attachments/assets/d9995ad7-8828-409b-b5d8-8b0bc58b1ee2" />

<img width="1186" height="608" alt="Output 3" src="https://github.com/user-attachments/assets/cc5eb293-0116-40b8-8ddf-125e6d6d7179" />

<img width="1138" height="659" alt="Output 4" src="https://github.com/user-attachments/assets/08b9bbd7-9f0a-4c45-b151-e7f9d9e956d0" />

<img width="1221" height="668" alt="Output 5" src="https://github.com/user-attachments/assets/9d437b36-3602-4acf-abb7-a290af7cc56d" />

<img width="1051" height="636" alt="Output 6" src="https://github.com/user-attachments/assets/0a095502-4cf1-4f7f-b0ed-d7e8f73858e9" />


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
This project is licensed under the MIT License.

## Author

Abhinav Dixit

Python Developer | Data & ML Enthusiast
