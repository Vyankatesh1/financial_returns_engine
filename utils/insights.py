def generate_insights(metrics: dict):
    insights = []

    if metrics["total_return"] > 0:
        insights.append("The portfolio generated positive total returns.")
    else:
        insights.append("The portfolio experienced an overall loss.")

    if metrics["cagr"] > 0.1:
        insights.append("The portfolio shows strong annualized growth.")
    elif metrics["cagr"] > 0:
        insights.append("The portfolio shows moderate growth.")
    else:
        insights.append("The portfolio shows negative annualized growth.")

    if metrics["volatility"] > 0.2:
        insights.append("Portfolio volatility is high, indicating higher risk.")
    else:
        insights.append("Portfolio volatility is within a stable range.")

    if metrics["sharpe_ratio"] > 1:
        insights.append("Risk-adjusted returns are strong.")
    elif metrics["sharpe_ratio"] > 0:
        insights.append("Risk-adjusted returns are acceptable.")
    else:
        insights.append("Risk-adjusted returns are weak.")

    return insights