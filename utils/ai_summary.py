# utils/ai_summary.py

def generate_ai_summary(metrics: dict):
    summary = []

    # Performance interpretation
    if metrics["total_return"] > 0:
        summary.append(
            f"The portfolio delivered a total return of {metrics['total_return']*100:.1f}%, indicating positive overall performance."
        )
    else:
        summary.append(
            f"The portfolio declined by {abs(metrics['total_return'])*100:.1f}%, reflecting negative performance over the period."
        )

    # Growth quality
    if metrics["cagr"] > 0.12:
        summary.append(
            "Annualized growth is strong, suggesting effective capital appreciation."
        )
    elif metrics["cagr"] > 0:
        summary.append(
            "Annualized growth is moderate, indicating steady portfolio expansion."
        )
    else:
        summary.append(
            "Negative annualized growth suggests capital erosion over time."
        )

    # Risk & volatility
    if metrics["volatility"] > 0.2:
        summary.append(
            "Volatility levels are elevated, implying higher risk exposure."
        )
    else:
        summary.append(
            "Volatility remains controlled, indicating stable return behavior."
        )

    # Risk-adjusted performance
    if metrics["sharpe_ratio"] > 1:
        summary.append(
            "Risk-adjusted returns are strong, demonstrating efficient compensation for risk."
        )
    elif metrics["sharpe_ratio"] > 0:
        summary.append(
            "Risk-adjusted returns are acceptable but could be improved."
        )
    else:
        summary.append(
            "Risk-adjusted returns are weak, suggesting inefficiency in risk-taking."
        )

    return " ".join(summary)