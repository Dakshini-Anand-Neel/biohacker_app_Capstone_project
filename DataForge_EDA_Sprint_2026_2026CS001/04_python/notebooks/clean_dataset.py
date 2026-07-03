import pandas as pd

def clean_data(df):
    # 1. Remove duplicates
    df = df.drop_duplicates()
    
    # 2. Drop columns with > 50% missing values
    threshold = len(df) * 0.5
    df = df.dropna(thresh=threshold, axis=1)
    
    # 3. Fill missing numeric values with median
    numeric_cols = df.select_dtypes(include=['number']).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
    
    # 4. Fill missing categorical values
    cat_cols = df.select_dtypes(include=['object', 'category']).columns
    df[cat_cols] = df[cat_cols].fillna("Unknown")
    
    # 5. Convert date columns and extract features
    for col in df.columns:
        if 'date' in col.lower():
            df[col] = pd.to_datetime(df[col], errors='coerce')
            df[f'{col}_month'] = df[col].dt.month
            df[f'{col}_year'] = df[col].dt.year
            
    return df