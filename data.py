import pandas as pd

def load_data():
    return pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        'Sales': [1000, 1200, 900, 1500, 1800, 1700, 1600, 2000, 2200, 1900, 2100, 2500],
        'Expenses': [800, 850, 750, 950, 1000, 1100, 1200, 1300, 1400, 1200, 1100, 1000],
        'Customers': [100, 120, 115, 130, 140, 150, 160, 170, 180, 175, 165, 190]
    })