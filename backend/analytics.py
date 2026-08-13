import numpy as np
import pandas as pd
from scipy.stats import norm

def calculate_portfolio_metrics(weights: list[float], returns_data: dict, confidence_level: float = 0.95):
    """
    Computes portfolio risk metrics including Sharpe Ratio, Value at Risk (VaR),
    and Expected Shortfall (CVaR) using Parametric and Historical methodologies.
    """
    df = pd.DataFrame(returns_data)
    weights = np.array(weights)
    
    # Expected Portfolio Return & Volatility
    mean_returns = df.mean()
    cov_matrix = df.cov()
    
    portfolio_expected_return = np.sum(mean_returns * weights) * 252
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix * 252, weights)))
    
    # Sharpe Ratio (Assuming Risk-Free Rate = 2%)
    risk_free_rate = 0.02
    sharpe_ratio = (portfolio_expected_return - risk_free_rate) / portfolio_volatility
    
    # Value at Risk (Parametric VaR)
    z_score = norm.ppf(confidence_level)
    parametric_var = (z_score * portfolio_volatility) - portfolio_expected_return
    
    # Historical VaR & Expected Shortfall (CVaR)
    portfolio_historical_returns = df.dot(weights)
    historical_var = np.percentile(portfolio_historical_returns, (1 - confidence_level) * 100) * -1 * np.sqrt(252)
    
    tail_losses = portfolio_historical_returns[portfolio_historical_returns <= -historical_var / np.sqrt(252)]
    cvar = tail_losses.mean() * -1 * np.sqrt(252) if not tail_losses.empty else historical_var
    
    return {
        "expectedReturn": round(float(portfolio_expected_return), 4),
        "volatility": round(float(portfolio_volatility), 4),
        "sharpeRatio": round(float(sharpe_ratio), 4),
        "parametricVaR": round(float(parametric_var), 4),
        "historicalVaR": round(float(historical_var), 4),
        "conditionalVaR": round(float(cvar), 4)
    }
