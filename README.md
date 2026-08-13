# Portfolio Risk Analytics Engine (Full-Stack)

### ⚡ Quick Overview
- **What it does:** Calculates real-time portfolio risk metrics (Volatility, Sharpe Ratio, 95% Parametric VaR, Historical VaR, and CVaR/Expected Shortfall).
- **Architecture:** Next.js dashboard passes allocation vectors to a FastAPI backend executing vectorized NumPy/SciPy linear algebra in <20ms.
- **Data Model:** Runs on a 252-day simulated stochastic market dataset (40/30/30 asset split) to maintain compliance with institutional NDAs.

A full-stack quantitative portfolio risk engine built with Python (FastAPI, NumPy, Pandas, SciPy) and Next.js (React 18, TypeScript, Tailwind CSS). The application models portfolio variance, computes parametric and historical Value at Risk (VaR), and calculates Conditional VaR (CVaR / Expected Shortfall) across custom asset allocations.

> **Notice on Proprietary Codebase & Data Sanitization:** This repository represents a reconstructed, standalone implementation inspired by software workflows I developed in my professional role as Senior Investment Associate / CAi Champion. To adhere strictly to non-disclosure obligations and compliance standards, all proprietary risk models, internal API endpoints, client portfolio data, and firm-specific modules have been redacted or replaced with open-source numerical libraries (NumPy, SciPy) and simulated stochastic price histories.

## Technical Stack & Architecture

- **Backend:** Python 3.11+, FastAPI, NumPy, Pandas, SciPy (Parametric & Historical VaR modelling).
- **Frontend:** Next.js 14 (App Router), React 18, TypeScript, Tailwind CSS.
- **Communication:** RESTful JSON API using Async CORS middleware.

## Default Model & Synthetic Dataset

The engine's default evaluation runs on a benchmark dataset out of the box:
- **Synthetic Price History:** 252 simulated trading days ($M = 252$) generated via Gaussian stochastic returns to represent a 1-year trading horizon.
- **Asset Allocation:** 3-asset portfolio weighted at **40% / 30% / 30%** ($w = [0.4, 0.3, 0.3]$).
- **Confidence Horizon:** 1-day holding period evaluated at a **95% statistical confidence level**.

## Core Quantitative Features

1. **Portfolio Volatility & Sharpe Ratio:** Calculates annualized portfolio risk using co-variance matrices: $\sigma_p = \sqrt{w^T \Sigma w}$
2. **Parametric Value at Risk (VaR):** Computes 95% statistical maximum drawdown over a 252-day horizon assuming a Gaussian return distribution.
3. **Historical VaR & Conditional VaR (CVaR / Expected Shortfall):** Evaluates tail-risk events by evaluating empirical historical return distributions to quantify expected losses beyond the VaR threshold.

## Algorithmic Complexity & Optimization

- **Covariance Matrix Calculation:** $O(N^2 \cdot M)$ matrix multiplication optimized using vectorized C-contiguous memory layouts in NumPy.
- **Historical VaR Sorting:** $O(M \log M)$ Timsort algorithm for empirical quantile estimation across $M = 252$ trading days.
- **API Response Latency:** Sub-20ms execution budget for portfolio risk parameter evaluations.

## Local Setup & Installation

### Prerequisites
- **Python 3.11+**
- **Node.js 18+** & `npm`

---

### 1. Backend Setup (FastAPI)

Open a terminal window and run:

```bash
# Navigate to backend directory
cd backend

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate
# (On Windows, run: venv\Scripts\activate)

# Install dependencies and launch API server
pip install fastapi uvicorn numpy pandas scipy pydantic
uvicorn main:app --reload --port 8000
```
*The API server runs locally at `http://localhost:8000` (Interactive Swagger docs available at `http://localhost:8000/docs`).*

---

### 2. Frontend Setup (Next.js)

Open a **second terminal tab** and run:

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies and launch web application
npm install
npm run dev
```
*The web dashboard runs locally at `http://localhost:3000`.*
