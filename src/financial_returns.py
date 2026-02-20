# src/financial_returns.py
import numpy as np

class FinancialReturnsCalculator:
    def __init__(self, monthly_values):
        # Store monthly portfolio values
        self.monthly_values = monthly_values

    def total_return(self):
        # Total return over the full period
        return (self.monthly_values[-1] / self.monthly_values[0]) - 1

    def cagr(self):
        # Annualized growth rate
        months = len(self.monthly_values) - 1
        years = months / 12
        return (self.monthly_values[-1] / self.monthly_values[0]) ** (1 / years) - 1

    def volatility(self):
        # Monthly return volatility, annualized
        returns = np.diff(self.monthly_values) / self.monthly_values[:-1]
        return np.std(returns) * np.sqrt(12)

    def sharpe_ratio(self, risk_free_rate=0.02):
        # Risk-adjusted return
        returns = np.diff(self.monthly_values) / self.monthly_values[:-1]
        excess_returns = returns - (risk_free_rate / 12)
        return np.mean(excess_returns) / np.std(excess_returns)