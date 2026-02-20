from utils.ai_summary import generate_ai_summary
from fastapi import FastAPI, UploadFile, File
import pandas as pd
import io

from src.financial_returns import FinancialReturnsCalculator
from utils.validators import validate_monthly_data
from utils.insights import generate_insights

app = FastAPI(title="BlackRock Financial Returns Engine")

# Health check
@app.get("/health")
def health():
    return {"status": "ok"}

# Existing GET endpoint (keep it)
@app.get("/calculate")
def calculate_from_sample():
    df = pd.read_csv("data/sample_input.csv")
    validate_monthly_data(df)

    values = df["portfolio_value"].tolist()
    calc = FinancialReturnsCalculator(values)

    metrics = {
        "total_return": round(calc.total_return(), 4),
        "cagr": round(calc.cagr(), 4),
        "volatility": round(calc.volatility(), 4),
        "sharpe_ratio": round(calc.sharpe_ratio(), 4),
    }

    return {
    "metrics": metrics,
    "insights": generate_insights(metrics),
    "ai_summary": generate_ai_summary(metrics)
    }
    

# 🔥 NEW: POST endpoint with CSV upload
@app.post("/calculate/upload")
def calculate_from_upload(file: UploadFile = File(...)):
    # Read uploaded CSV file
    contents = file.file.read()
    df = pd.read_csv(io.StringIO(contents.decode("utf-8")))

    # Validate input data
    validate_monthly_data(df)

    # Extract monthly portfolio values
    values = df["portfolio_value"].tolist()
    calc = FinancialReturnsCalculator(values)

    metrics = {
        "total_return": round(calc.total_return(), 4),
        "cagr": round(calc.cagr(), 4),
        "volatility": round(calc.volatility(), 4),
        "sharpe_ratio": round(calc.sharpe_ratio(), 4),
    }

    return {
    "metrics": metrics,
    "insights": generate_insights(metrics),
    "ai_summary": generate_ai_summary(metrics)
    }