import pandas as pd

def validate_monthly_data(df: pd.DataFrame):
    # Check required column
    if "portfolio_value" not in df.columns:
        raise ValueError("Missing 'portfolio_value' column")

    # Check for empty values
    if df["portfolio_value"].isnull().any():
        raise ValueError("Portfolio values contain missing data")

    # Portfolio values must be positive
    if (df["portfolio_value"] <= 0).any():
        raise ValueError("Portfolio values must be positive")

    return True
