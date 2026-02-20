import sys
import os

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.financial_returns import FinancialReturnsCalculator

initial_investment = 10000

monthly_values = [
    10000, 10200, 10150, 10400, 10600, 10800,
    10750, 11000, 11200, 11500, 11700, 12000
]

monthly_cashflows = [
    -10000, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 12000
]

calculator = FinancialReturnsCalculator(
    initial_investment=initial_investment,
    monthly_values=monthly_values,
    monthly_cashflows=monthly_cashflows,
    risk_free_rate=0.02
)

print("Summary:")
print(calculator.summary())
print("NPV:", round(calculator.npv(0.08), 2))
print("IRR:", round(calculator.irr(), 4))
