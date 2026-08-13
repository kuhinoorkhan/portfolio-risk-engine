from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
from analytics import calculate_portfolio_metrics

app = FastAPI(title="Quant Portfolio Risk Engine")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PortfolioRequest(BaseModel):
    weights: list[float]
    assets: list[str]

@app.post("/api/v1/analyze")
async def analyze_portfolio(request: PortfolioRequest):
    if not np.isclose(sum(request.weights), 1.0):
        raise HTTPException(status_code=400, detail="Portfolio weights must sum to 1.0")
    
    # Simulated daily returns for standard backtesting (252 trading days)
    np.random.seed(42)
    simulated_returns = {
        asset: np.random.normal(0.0005, 0.015, 252) for asset in request.assets
    }
    
    metrics = calculate_portfolio_metrics(request.weights, simulated_returns)
    return {"status": "success", "data": metrics}
