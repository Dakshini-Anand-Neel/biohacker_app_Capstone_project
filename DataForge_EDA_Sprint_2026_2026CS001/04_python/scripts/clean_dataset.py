import pandas as pd

def clean_data(df):
    df = df.drop_duplicates()
    
    threshold = len(df) * 0.5
    df = df.dropna(thresh=threshold, axis=1)
    
    numeric_cols = df.select_dtypes(include=['number']).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
    
    cat_cols = df.select_dtypes(include=['object', 'category']).columns
    df[cat_cols] = df[cat_cols].fillna("Unknown")
    
    # Replace 'date_column' with your actual date column name
    if 'date_column' in df.columns:
        df['date_column'] = pd.to_datetime(df['date_column'])
        df['month'] = df['date_column'].dt.month
        df['year'] = df['date_column'].dt.year
    
    # Replace 'sales' and 'cost' with your actual numerical column names
    if 'sales' in df.columns and 'cost' in df.columns:
        df['profit'] = df['sales'] - df['cost']
        df['profit_margin'] = df['profit'] / df['sales']
        
    return df