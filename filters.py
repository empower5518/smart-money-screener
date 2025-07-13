import pandas as pd

def apply_all_filters(price_range, min_roe, max_de_ratio, rsi_threshold, beta_threshold, market_caps):
    # Simulated data – replace with real data fetch
    data = [
        {"Symbol": "ABC", "Price": 320, "ROE": 18, "DebtEquity": 0.3, "RSI": 65, "Beta": 1.1, "MarketCapCategory": "Midcap"},
        {"Symbol": "XYZ", "Price": 510, "ROE": 20, "DebtEquity": 0.2, "RSI": 70, "Beta": 1.0, "MarketCapCategory": "Largecap"},
    ]
    df = pd.DataFrame(data)
    filtered = df[
        (df['Price'] >= price_range[0]) &
        (df['Price'] <= price_range[1]) &
        (df['ROE'] >= min_roe) &
        (df['DebtEquity'] <= max_de_ratio) &
        (df['RSI'] >= rsi_threshold) &
        (df['Beta'] <= beta_threshold) &
        (df['MarketCapCategory'].isin(market_caps))
    ]
    return filtered
